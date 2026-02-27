from product_designer import build_product_structure
from pitch_generator import generate_pitch

if __name__ == "__main__":

    industry = input("Enter industry: ")
    problem = input("Describe a real problem in that industry: ")

    prompt = build_product_structure(industry, problem)

    print("\n--- AI Product Design ---\n")

    result = generate_pitch(prompt)
    print(result)
