from django.http import JsonResponse

def api_root(request):
    base_url = "https://reimagined-couscous-x5r5xr764p4gcp4p7-8000.app.github.dev/"
    return JsonResponse({
        "users": base_url + "api/users/",
        "teams": base_url + "api/teams/",
        "activities": base_url + "api/activities/",
        "leaderboard": base_url + "api/leaderboard/",
        "workouts": base_url + "api/workouts/",
    })
