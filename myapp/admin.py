from django.contrib import admin
from .models import Campaign, CampaignAcceptance, Deliverable


# -----------------------------------------------------------
# 1. Campaign Admin
# -----------------------------------------------------------
@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product_name', 'brand', 'product_type',
        'target_pet_type', 'min_follower_count',
        'required_creator_count', 'campaign_status',
        'requested_at', 'application_deadline_at'
    )
    list_display_links = ('id', 'product_name')

    list_filter = (
        'campaign_status',
        'product_type',
        'target_pet_type',
        'brand',
    )

    search_fields = (
        'product_name',
        'brand__name',
        'brand__email',
        'product_type'
    )

    ordering = ('-requested_at',)
    list_per_page = 20



# -----------------------------------------------------------
# 2. CampaignAcceptance Admin
# -----------------------------------------------------------
@admin.register(CampaignAcceptance)
class CampaignAcceptanceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'creator', 'campaign',
        'acceptance_status',
        'applied_at', 'selected_at'
    )
    list_display_links = ('id', 'creator', 'campaign')

    list_filter = (
        'acceptance_status',
        'campaign__product_type',
        'campaign__brand',
        'creator__pet_type',
    )

    search_fields = (
        'creator__name',
        'creator__username',
        'campaign__product_name'
    )

    ordering = ('-applied_at',)
    list_per_page = 20



# -----------------------------------------------------------
# 3. Deliverable Admin
# -----------------------------------------------------------
@admin.register(Deliverable)
class DeliverableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'acceptance',
        'get_creator_name',
        'get_campaign_name',
        'posted_at',
        'deliverable_status',
        'brand_approval_at',
        'settlement_status'
    )
    list_display_links = ('id', 'acceptance')

    list_filter = (
        'deliverable_status',
        'settlement_status',
        'acceptance__campaign__brand',
    )

    search_fields = (
        'acceptance__creator__name',
        'acceptance__creator__username',
        'acceptance__campaign__product_name',
    )

    ordering = ('-posted_at',)
    list_per_page = 20

    # 추가: 리스트에 크리에이터/캠페인 이름을 직접 보여주기 위한 커스텀 필드
    def get_creator_name(self, obj):
        return obj.acceptance.creator.name
    get_creator_name.short_description = 'Creator'

    def get_campaign_name(self, obj):
        return obj.acceptance.campaign.product_name
    get_campaign_name.short_description = 'Campaign'
