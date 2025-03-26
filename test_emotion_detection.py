import unittest
from final_project.EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_emotion_detector(self):
        # Test for joy
        response = emotion_detector("I am glad this happened")
        self.assertEqual(response['dominant_emotion'], "joy")
        
        # Test for anger
        response = emotion_detector("I am really mad about this")
        self.assertEqual(response['dominant_emotion'], "anger")
        
        # Test for disgust
        response = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response['dominant_emotion'], "disgust")
        
        # Test for sadness
        response = emotion_detector("I am so sad about this")
        self.assertEqual(response['dominant_emotion'], "sadness")
        
        # Test for fear
        response = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(response['dominant_emotion'], "fear")

if __name__ == "__main__":
    unittest.main()