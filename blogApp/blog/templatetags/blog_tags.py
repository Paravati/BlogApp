from django import template

register = template.Library()

from ..models import Post


@register.simple_tag()  # template marker which returns amount of published posts
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_post = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_post}


from django.db.models import Count

@register.simple_tag()
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
