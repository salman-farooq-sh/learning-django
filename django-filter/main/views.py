from django_filters.views import FilterView
from furl import furl

from .filters import BookFilter
from .models import Author


class BookFilterView(FilterView):
    template_name = 'book_filter.html'
    filterset_class = BookFilter
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        def add_get_parameter(url, parameter):
            parameter_name, parameter_value = parameter.split('=', maxsplit=2)
            f = furl(url)
            f.args[parameter_name] = parameter_value
            return f.url

        context = super().get_context_data(*args, **kwargs)

        request_url = self.request.get_full_path(force_append_slash=True)
        page_obj = context['page_obj']
        context['page_urls'] = {
            'first': add_get_parameter(
                request_url, f'page=1'
            ),
            'previous': add_get_parameter(
                request_url, f'page={page_obj.previous_page_number() if page_obj.has_previous() else ""}'
            ),
            'next': add_get_parameter(
                request_url, f'page={page_obj.next_page_number() if page_obj.has_next() else ""}'
            ),
            'last': add_get_parameter(
                request_url, f'page={page_obj.paginator.num_pages}'
            ),
        }

        return context


class AuthorFilterView(FilterView):
    model = Author
    filterset_fields = ['name', 'date_of_birth']
    template_name = 'author_filter.html'
    paginate_by = 20
