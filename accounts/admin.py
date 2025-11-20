from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # 관리자 리스트에 보여줄 필드
    list_display = (
        'id', 'username', 'name', 'email',
        'account_type', 'pet_type', 'follower_count',
        'brand_pet_focus', 'is_active'
    )

    # 클릭해서 상세 페이지로 들어갈 수 있는 필드
    list_display_links = ('id', 'username', 'name')

    # 오른쪽 필터 영역
    list_filter = (
        'account_type',
        'pet_type',
        'brand_pet_focus',
        'is_active',
        'is_staff'
    )

    # 검색 가능 필드
    search_fields = (
        'username',
        'name',
        'email',
        'pet_type',
        'sns_handle'
    )

    # 한 페이지에 보일 유저 수
    list_per_page = 20

    # 정렬 기준
    ordering = ('-id',)

    # admin 변경폼에서 보이는 필드 그룹 구성
    fieldsets = (
        ("기본 정보", {
            "fields": (
                'username',
                'password',
                'name',
                'email',
                'phone_number',
                'account_type',
            )
        }),
        ("Brand 전용 정보", {
            "fields": (
                'brand_pet_focus',
            ),
            "classes": ('collapse',),  # 접어서 보기
        }),
        ("Creator 전용 정보", {
            "fields": (
                'address',
                'pet_type',
                'sns_handle',
                'sns_url',
                'total_post_count',
                'follower_count',
            ),
            "classes": ('collapse',),
        }),
        ("권한 설정", {
            "fields": (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions',
            )
        }),
        ("중요 날짜", {
            "fields": ('last_login', 'date_joined')
        }),
    )
