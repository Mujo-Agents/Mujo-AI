class StyleBlender:
    def blend(self, cultural_elements, preferences):
        print("Blending cultural elements with user preferences...")
        return {
            "patterns": cultural_elements["patterns"] + preferences,
            "colors": cultural_elements["colors"],
            "symbols": cultural_elements["symbols"]
        }
