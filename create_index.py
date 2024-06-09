from twelvelabs import TwelveLabs
import os

api_key = os.environ.get("TLABS")


client = TwelveLabs(api_key = api_key)

engines = [
        {
          "name": "marengo2.6",
          "options": ["visual", "conversation", "text_in_video", "logo"]
        },
        {
            "name": "pegasus1",
            "options": ["visual", "conversation"]
        }
  ]

index = client.index.create(
    name = "tlabs2",
    engines=engines,
    addons=["thumbnail"] # Optional
)
print(f"A new index has been created: id={index.id} name={index.name} engines={index.engines}")
