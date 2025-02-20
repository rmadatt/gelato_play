# views.py
from flask import Blueprint, render_template, request
from .models import GlossaryAgent

# Use the blueprint defined in urls.py
bp = Blueprint('views', __name__, url_prefix='/')

# Initialize the GlossaryAgent
glossary_agent = GlossaryAgent()

@bp.route('/', methods=['GET'])
def home():
    """Render the homepage with a list of glossary terms."""
    terms = glossary_agent.list_terms()
    if not terms:  # Seed with some terms if empty
        glossary_agent.learn_term("Machine Learning")
        glossary_agent.learn_term("Generative AI")
        terms = glossary_agent.list_terms()
    return render_template('home.html', terms=terms)

@bp.route('/term', methods=['GET', 'POST'])
def term_detail():
    """Handle term explanation requests."""
    if request.method == 'POST':
        term = request.form.get('term', '').strip()
        if term:
            explanation = glossary_agent.explain_term(term)
            return render_template('term.html', explanation=explanation)
    # GET request: show a form or default term
    default_term = "Chatbot"
    explanation = glossary_agent.explain_term(default_term)
    return render_template('term.html', explanation=explanation)
