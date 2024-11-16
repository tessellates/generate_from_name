import torch
from diffusers import StableDiffusionPipeline
import sys

def prompt(keywords, name):
    print(f"started: {keywords}, {name}")
    torch.cuda.empty_cache()  # Clear unused memory
    # Load the pre-trained model pipeline
    #pipe = StableDiffusionPipeline.from_pretrained("stable-diffusion-v1-5/stable-diffusion-v1-5", use_auth_token=True, low_cpu_mem_usage=True)
    from diffusers import DiffusionPipeline

    pipe = DiffusionPipeline.from_pretrained("UnfilteredAI/NSFW-Flux-v1")
    pipe.to("mps")
    # Move the pipeline to MPS for GPU processing
    # Function to generate an image
    def generate_image(prompt):
        image = pipe(prompt, 208, 272).images[0]
        return image

    # Generate an example image
    prompt = f"{keywords}, hand drawn, colorfull"
    image = generate_image(prompt)

    # Save the generated image
    image.save(f"{name}.png")

def main():
    # Ensure the script has the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <image_path> <mask_path> <output_name>")
        sys.exit(1)

    # Get arguments from the command line
    image_path = sys.argv[1]
    keywords = sys.argv[1]
    name = sys.argv[2]

    # Call the mask_image function with the provided arguments
    prompt(keywords, name)

if __name__ == "__main__":
    main()
