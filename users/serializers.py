from rest_framework import serializers
from agencies.models import Affiliation, Branch, BusinessArea

from agencies.serializers import (
    AffiliationSerializer,
    MiniBASerializer,
    MiniBranchSerializer,
    StaffProfileBASerializer,
    StaffProfileBranchSerializer,
    TinyAgencySerializer,
    TinyBranchSerializer,
    TinyBusinessAreaSerializer,
)
from medias.models import UserAvatar
from medias.serializers import UserAvatarSerializer
from projects.models import ProjectMember
from .models import (
    EducationEntry,
    EmploymentEntry,
    PublicStaffProfile,
    StaffProfileProjectEntry,
    User,
    UserWork,
    UserProfile,
)


class PrivateTinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "is_superuser",
            "is_aec",
            # "is_biometrician",
            # "is_herbarium_curator",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        ]


class MiniUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "first_name",
            "last_name",
            "username",
            "email",
            "is_active",
            "is_superuser",
        )


class TinyUserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="work.role")
    branch = TinyBranchSerializer(source="work.branch")
    business_area = TinyBusinessAreaSerializer(source="work.business_area")
    image = UserAvatarSerializer(source="profile.image")
    affiliation = AffiliationSerializer(source="work.affiliation")

    class Meta:
        model = User
        fields = (
            "pk",
            "first_name",
            "last_name",
            "username",
            "email",
            "is_active",
            "is_superuser",
            # "is_biometrician",
            # "is_herbarium_curator",
            "is_aec",
            "is_staff",
            "image",
            "role",
            "branch",
            "business_area",
            "affiliation",
        )


class TinyStaffProfileSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="work.role")
    branch = StaffProfileBranchSerializer(source="work.branch")
    # business_area = StaffProfileBASerializer(source="work.business_area")

    class Meta:
        model = User
        fields = (
            "pk",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "role",
            "branch",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]


class TinyUserProfileSerializer(serializers.ModelSerializer):
    # user = TinyUserSerializer(read_only=True)
    # image = UserAvatarSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = (
            "pk",
            "user",
            # "image",
            "title",
            "middle_initials",
            "about",
            "curriculum_vitae",
            "expertise",
        )


class UserProfileSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer(read_only=True)
    image = UserAvatarSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"


class TinyUserWorkSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer()
    agency = TinyAgencySerializer()
    branch = TinyBranchSerializer()
    business_area = TinyBusinessAreaSerializer()
    affiliation = AffiliationSerializer()

    class Meta:
        model = UserWork
        fields = (
            "pk",
            "user",
            "role",
            "agency",
            "branch",
            "business_area",
            "affiliation",
        )


class UserWorkSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer()
    agency = TinyAgencySerializer()
    branch = TinyBranchSerializer()
    business_area = TinyBusinessAreaSerializer()
    affiliation = AffiliationSerializer()

    class Meta:
        model = UserWork
        fields = "__all__"


class UserWorkAffiliationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWork
        fields = [
            "affiliation",
        ]


class UpdatePISerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    title = serializers.CharField(
        source="profile.title",
        allow_blank=True,
        allow_null=True,
    )
    phone = serializers.CharField(
        source="contact.phone",
        allow_blank=True,
        allow_null=True,
    )
    fax = serializers.CharField(
        source="contact.fax",
        allow_blank=True,
        allow_null=True,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "title",
            "fax",
            "phone",
        )

    def update(self, instance, validated_data):
        profile_data = validated_data.pop("profile", None)
        contact_data = validated_data.pop("contact", None)

        if profile_data:
            profile = instance.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()

        if contact_data:
            contact = instance.contact
            for attr, value in contact_data.items():
                setattr(contact, attr, value)
            contact.save()

        return instance


class UpdateProfileSerializer(serializers.ModelSerializer):
    image = serializers.PrimaryKeyRelatedField(
        source="profile.image", queryset=UserAvatar.objects.all(), required=False
    )
    about = serializers.CharField(
        source="profile.about",
        allow_blank=True,
        allow_null=True,
        required=False,
    )
    expertise = serializers.CharField(
        source="profile.expertise",
        allow_blank=True,
        allow_null=True,
        required=False,
    )

    class Meta:
        model = User
        fields = (
            "image",
            "about",
            "expertise",
        )

    def update(self, instance, validated_data):
        profile_data = validated_data.pop("profile", None)

        if profile_data:
            profile = instance.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()

        return instance


class UpdateMembershipSerializer(serializers.ModelSerializer):
    branch = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=False
    )
    business_area = serializers.PrimaryKeyRelatedField(
        queryset=BusinessArea.objects.all(), required=False
    )
    affiliation = serializers.PrimaryKeyRelatedField(
        queryset=Affiliation.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = UserWork
        fields = (
            "affiliation",
            "branch",
            "business_area",
        )


class StaffProfileUserSerializer(serializers.ModelSerializer):
    branch_name = serializers.SerializerMethodField()
    business_area_name = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    def get_branch_name(self, obj):
        return obj.work.branch.name if obj.work and obj.work.branch else None

    def get_business_area_name(self, obj):
        return (
            obj.work.business_area.name if obj.work and obj.work.business_area else None
        )

    def get_title(self, obj):
        return obj.profile.title if obj.profile else None

    class Meta:
        model = User
        fields = (
            "pk",
            "first_name",
            "last_name",
            "email",
            "title",
            "branch_name",
            "business_area_name",
        )


class EmploymentEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentEntry
        exclude = ("public_profile",)


class EducationEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationEntry
        exclude = ("public_profile",)


class ProjectEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffProfileProjectEntry
        fields = (
            "public_profile",
            "project_membership",
            "flavour_text",
        )


class ProjectMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = ("project",)

    project = serializers.SerializerMethodField()

    def get_project(self, obj):
        return {
            "title": obj.project.title,
            "description": obj.project.description,
            "start_date": obj.project.start_date,
            "end_date": obj.project.start_date,
        }


class StaffProfileSerializer(serializers.ModelSerializer):
    user = StaffProfileUserSerializer(read_only=True)
    project_memberships = ProjectMembershipSerializer(
        many=True, read_only=True, source="projects"
    )
    employment = EmploymentEntrySerializer(many=True, read_only=True)
    education = EducationEntrySerializer(many=True, read_only=True)

    def get_title():
        pass

    def get_first_name():
        pass

    def get_last_name():
        pass

    def get_business_area():
        pass

    def get_branch():
        pass

    def get_user_pk():
        pass

    # I want to serialize project_memberships to get the project.title and project.description and project.year only and return that

    # I want to serialize employment so it doesnt return the staff profile part (should I just use related name with onetomany instead of fk?)

    # I want to serialize education so it doesnt return the staff profile part (should I just use related name with onetomany instead of fk?)

    class Meta:
        model = PublicStaffProfile
        fields = (
            "pk",
            "is_hidden",
            "aucode",
            "user",
            "dbca_position_title",
            "keyword_tags",
            "about_me",
            "expertise",
            "education",
            "project_memberships",
            "employment",
            "publications",
        )


class ProfilePageSerializer(serializers.ModelSerializer):
    image = UserAvatarSerializer(source="profile.image")
    role = serializers.CharField(source="work.role")

    expertise = serializers.CharField(source="profile.expertise")
    title = serializers.CharField(source="profile.title")
    about = serializers.CharField(source="profile.about")
    agency = TinyAgencySerializer(source="work.agency")
    branch = MiniBranchSerializer(source="work.branch")
    business_area = MiniBASerializer(source="work.business_area")
    affiliation = AffiliationSerializer(source="work.affiliation")

    phone = serializers.CharField(source="contact.phone")
    fax = serializers.CharField(source="contact.fax")

    class Meta:
        model = User
        fields = (
            "pk",
            "first_name",
            "last_name",
            "username",
            "email",
            "is_superuser",
            # "is_biometrician",
            # "is_herbarium_curator",
            "is_aec",
            "is_staff",
            "is_active",
            "date_joined",
            "image",
            "role",
            "expertise",
            "about",
            "agency",
            "branch",
            "business_area",
            "title",
            "phone",
            "fax",
            "affiliation",
            "business_areas_led",
        )
