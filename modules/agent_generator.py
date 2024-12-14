from modules.cultural_analysis import CulturalAnalyzer
from modules.style_blender import StyleBlender
from modules.aesthetics_evaluator import AestheticsEvaluator

class AgentGenerator:
    def generate_agent(self, user_data):
        analyzer = CulturalAnalyzer()
        cultural_elements = analyzer.analyze(user_data["culture"])

        blender = StyleBlender()
        blended_styles = blender.blend(cultural_elements, user_data["preferences"])

        evaluator = AestheticsEvaluator()
        is_approved = evaluator.evaluate(blended_styles)

        if is_approved:
            agent = {
                "name": f"Agent_{user_data['user_name']}",
                "style": blended_styles
            }
            return agent
        else:
            raise ValueError("Failed to create an aesthetically pleasing agent.")
