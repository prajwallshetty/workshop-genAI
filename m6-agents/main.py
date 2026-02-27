from agent_brain import resume_agent

if __name__ == "__main__":

    print("Enter Resume Text:")
    resume = input()

    print("\nEnter Job Description:")
    jd = input()

    print("\n--- Agent Analysis ---\n")

    result = resume_agent(resume, jd)
    print(result)
