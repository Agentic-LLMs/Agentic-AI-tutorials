# Practical Assignment: Multi-Agent Hospital Simulation

This assignment accompanies the section **Tools** and focuses on building a simplified, agentic hospital intelligence system. You will implement a multi-agent simulation in which planner and executor agents coordinate diagnostic tasks via a shared context.

The goal is **not** to build a clinically valid system, but to understand how agentic architectures work in high-risk domains, how agents coordinate via shared state, and where limitations and safety concerns arise.

---

## Learning Goals

By completing this assignment, you will:

- Design and implement a multi-agent system in Python
- Model agent roles such as planners and executors
- Use simple ML models as tools inside an agentic workflow
- Work with shared context / memory between agents
- Analyze behaviour, limitations, and risks of agentic systems in medicine

---

## Assignment Overview

You will simulate a hospital diagnostic workflow with:

- **Planner agents**  
  Decide which diagnostic pathway a patient case should follow.

- **Executor agents**  
  Run a diagnostic model (e.g. diabetes, heart disease, breast cancer) and report results.

- **Shared Context (MCP-like layer)**  
  A central data structure used by all agents to read/write tasks and results.

The simulation runs in discrete steps and logs how cases flow through the system.

---


## Environment Setup

### 1. Create a Virtual Environment

We strongly recommend using a virtual environment, use Python 3.10 or higher.

```bash
python3 -m venv venv
````

Activate it:

* **Linux / macOS**

```bash
source venv/bin/activate
```

* **Windows**

```bash
venv\Scripts\activate
```

### 2. Install Dependencies

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Step-by-Step Tasks

### Step 0: Train Diagnostic Models

Use public datasets to train **simple classifiers** (e.g. in our case random forest):

* Diabetes (Pima Indians dataset)
* Breast cancer (from `sklearn.datasets`)
* Heart disease (UCI)

```bash
python 0_train_models.py
```

---

### Step 2: Understand the baseline

The baseline code is provided in `1_basic_mcp.py`.
Read and execute the baseline code to understand what is happening.
Specifically pay attention to:


#### Shared Context (MCP)

A shared context object that:

* Stores incoming patient cases
* Stores assigned diagnostic tasks
* Stores diagnostic results

All agents interact **only through this context**, not directly with each other.

#### Planner Agent

* Reads unassigned cases from the context
* Decides which diagnostic domain applies
* Creates diagnostic tasks in the context

#### Executor Agent

* Reads tasks assigned to its specialty
* Loads the corresponding ML model
* Produces predictions
* Writes results back to the context

---

### Step 3: Run the baseline Simulation

Run the baseline code and observe what happens.  

How well is it performing?  
Is this a realistic scenario?  
What can be improved in this scenario?  
Is the accuracy of the trained models fairly assessed?

---

### Step 4: Replace the simple planners with an LLM agent


To make the simulation more meaningful and realistic, we now replace the 3 planner agents with 1 planner LLM agent.
The structure of the code is already given in `2_llm_mcp.py`. Notice some small changes and the extra function `make_case_text` (which you are not allowed to modify). This function creates a textual representation of a case, where a case is now a combination of records from all 3 data sets.

Your task is to implement the `step()` function of the `LLMPlannerAgent`.
The LLM planner agent should decide which ML models to use (can be multiple), in addition it should decide which is the primary target (most likely disease) per case.  You should also implement `call_llm_fn()` with a real LLM, either using ollama or OpenAI/Gemini. Note that a google account gives you limited free access to the Gemini API. 

In addition, we want to see how the LLM planner agent is performing, for this you need to write an analysis code snippet to produce the necessary tables and plots.

---

## Report Requirements

Submit a short report (PDF, max ~6 pages) that includes:

* System architecture overview with an explanation of the baseline in your own words
* Answer to the questions of Step 3 (see above)
* Description of the new LLM agent and which design choices you made.
* Results and plots
* Discussion of limitations
* Reflection on safety, fairness and transparency of these assistants.

---

## Optional Extensions (Bonus)

You may optionally:

* Do the sampling of patients more realisticly instead of randomly combining cases from the 3 datasets.
* Add another disease from the UCI repository  
* Add an evaluator or verifier agent  
* Simulate human-in-the-loop decision making  
* Add uncertainty thresholds and abstention  
* Introduce retrieval from external knowledge sources

These are not required, but can improve your grade if done well.

---

## Submission

Submit:

* A zip file with all the code and a readme on how to run.
* Trained model files or instructions to reproduce them.
* The final report as PDF.

Make sure your code runs from a clean unzip following the instructions above.

---

## Important Notes

* This assignment is **educational**, not clinical.
* Do not claim medical validity.
* Clear structure, reproducibility and reflection matter more than raw performance.

Good luck — and treat your agents responsibly.


#### Acknowledgement

This assignment is partly based on the Tutorial by Ayushman Pranav: https://medium.com/@AyushmanPranav/modeling-hospital-intelligence-with-mcp-a-multi-agent-diagnostic-simulation-afeff0dd885d 