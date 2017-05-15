from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q').strip()
        if len(querystring) == 0:
            return redirect('/search/')

        try:
            search_type = request.GET.get('type')
            if search_type not in ['ngolist']:
                search_type = 'ngolist'

        except Exception:
            search_type = 'ngolist'

        count = {}
        results = {}
        results['ngolist'] = Ngo.objects.filter(post__icontains=querystring,
                                              parent=None)

        count['ngolist'] = results['ngolist'].count()

        return render(request, 'search/results.html', {
            'hide_search': True,
            'querystring': querystring,
            'active': search_type,
            'count': count,
            'results': results[search_type],
        })
    else:
        return render(request, 'search/search.html', {'hide_search': True})
