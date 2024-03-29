from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("index-2/", index2, name="index2"),
    path("index-3/", index3, name="index3"),
    path("index-4/", index4, name="index4"),
    path("index-5/", index5, name="index5"),
    path("profile/", profile, name="profile"),
    path("wishlist/", profile, name="wishlist"),
    path("compare/", profile, name="compare"),
    path("shop/", profile, name="shop"),
    path("contact/", contact, name="contact"),
    path("404/", error, name="404"),
    path("about/", about, name="about"),
    path("blog-details/", blog_details, name="blog-details"),
    path("blog-details2/", blog_details2, name="blog-details2"),
    path("blog-grid/", blog_grid, name="blog-grid"),
    path("blog/", blog, name="blog"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("coupon/", coupon, name="coupon"),
    path("forgot/", forgot, name="forgot"),
    path("order/", order, name="order"),
    path("product-details-countdown/", product_details_countdown, name="product-details-countdown"),
    path("product-details-gallery/", product_details_gallery, name="product-details-gallery"),
    path("product-details-list/", product_details_list, name="product-details-list"),
    path("product-details-presentation/", product_details_presentation, name="product-details-presentation"),
    path("product-details-progress/", product_details_progress, name="product-details-progress"),
    path("product-details-slider/", product_details_slider, name="product-details-slider"),
    path("product-details-swatches/", product_details_swatches, name="product-details-swatches"),
    path("product-details-video/", product_details_video, name="product-details-video"),
    path("product-details/", product_details, name="product-details"),
    path("shop-1600/", shop_1600, name="sho-1600p"),
    path("shop-category/", shop_category, name="shop-category"),
    path("shop-filter-dropdown/", shop_filter_dropdown, name="shop-filter-dropdown"),
    path("shop-filter-offcanvas/", shop_filter_offcanvas, name="shop-filter-offcanvas"),
    path("shop-full-width/", shop_full_width, name="shop-category"),
    path("shop-infinite-scroll/", shop_infinite_scroll, name="shop-infinite-scroll"),
    path("shop-list/", shop_list, name="shop-list"),
    path("shop-load-more/", shop_load_more, name="shop-category"),
    path("shop-masonary/", shop_masonary, name="shop-category"),
    path("shop-no-sidebar/", shop_no_sidebar, name="shop-no-sidebar"),
    path("shop-right-sidebar/", shop_right_sidebar, name="shop-right-sidebar"),
]