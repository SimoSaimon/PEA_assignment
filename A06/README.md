# Confidence Intervals
___

### Overview
This report examines two server scenarios where jobs are executed individually in arrival order without interruptions. The inter-arrival and service time distributions for each scenario are specified, and the performance indices are evaluated with 95% confidence intervals and a 2% relative error.

---

### Scenarios

#### Scenario I
- **Arrival Distribution**: Two-stage hyper-exponential
  - λ₁ = 0.025
  - λ₂ = 0.1
  - p₁ = 0.35
- **Service Distribution**: Weibull
  - Shape (k) = 0.333
  - Scale (λ) = 2.5

#### Scenario II
- **Arrival Distribution**: Erlang
  - Stages (k) = 8
  - Rate (λ) = 1.25
- **Service Distribution**: Uniform
  - Range: a = 1, b = 10

---

### Results

For each scenario, batches of M = 5000 jobs were used to compute the 95% confidence intervals of the following performance indices, with a 2% relative error.

#### Scenario I

- **Utilization**: <span style="color:lightgreen;font-weight:bold">0.7301114756101802, 0.7317809487482906</span>
- **Throughput**: <span style="color:lightgreen;font-weight:bold">0.04855699920663156, 0.048593210974977444</span>
- **Average Number of Jobs in System**: <span style="color:lightgreen;font-weight:bold">21.317087404597146, 21.74761648048574</span>
- **Average Response Time**: <span style="color:lightgreen;font-weight:bold">438.5727573345932, 447.4135370252048</span>

- **Number of Batches (K) for Required Accuracy**: <span style="color:lightgreen;font-weight:bold">12060 iterations</span>

#### Scenario II

- **Utilization**: <span style="color:lightgreen;font-weight:bold">0.8574932888599173, 0.8605153275682179</span>
- **Throughput**: <span style="color:lightgreen;font-weight:bold">0.15604840424684432, 0.15644722785671186</span>
- **Average Number of Jobs in System**: <span style="color:lightgreen;font-weight:bold">1.575660233175678, 1.607074987437922</span>
- **Average Response Time**: <span style="color:lightgreen;font-weight:bold">10.089513571555935, 10.278160889792497</span>

- **Number of Batches (K) for Required Accuracy**: <span style="color:lightgreen;font-weight:bold">80 iterations</span>


---

### Python Script

Python script that calculates all the above values: [**A06.py**](A06.py)