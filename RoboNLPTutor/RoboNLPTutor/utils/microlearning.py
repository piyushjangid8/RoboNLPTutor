import random
from data.microlearning_tips import MICROLEARNING_TIPS

def get_random_tip(category=None):
    """Get a random microlearning tip for a specific category or any category"""
    if category and category in MICROLEARNING_TIPS:
        tips = MICROLEARNING_TIPS[category]
    else:
        # Flatten all tips into a single list
        tips = [tip for category in MICROLEARNING_TIPS.values() for tip in category]
    
    return random.choice(tips) if tips else None

def get_tips_for_category(category):
    """Get all tips for a specific category"""
    return MICROLEARNING_TIPS.get(category, [])

def format_tip_markdown(tip):
    """Format a tip into a nice markdown display"""
    return f"""
    <div style="background-color: #f8f9fa; padding: 1rem; border-radius: 10px; margin: 1rem 0;">
        <h4>{tip['emoji']} {tip['title']}</h4>
        <p>{tip['content']}</p>
        <pre><code>{tip['example']}</code></pre>
        <p>📚 <a href="{tip['resource_path']}">Learn more</a></p>
    </div>
    """
