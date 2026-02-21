"""
PlanIt: Multi-Agent AI Planner (Simulation Prototype)

This script demonstrates a simplified distributed multi-agent
architecture for intelligent trip and logistics planning.

PROJECT PURPOSE:
- Validate multi-agent architecture
- Demonstrate agent coordination
- Show weighted decision fusion
- Provide proof-of-concept simulation

NOTE:
This is a simulation prototype intended for academic validation,
not a real-time deployment system.
"""


# =========================================================
# Base Agent Class
# =========================================================
class BaseAgent:
    """
    Base class for all agents.
    Ensures modular and extensible architecture.
    """

    def __init__(self, name):
        self.name = name

    def process(self, data):
        raise NotImplementedError(
            "Each agent must implement the process() method"
        )


# =========================================================
# Preference Agent
# =========================================================
class PreferenceAgent(BaseAgent):
    """
    Interprets user priority and assigns optimization weights.
    """

    def process(self, user_input):
        print(f"[{self.name}] Processing user preferences...")

        weights = {
            "time_weight": 0.6 if user_input["priority"] == "fast" else 0.4,
            "cost_weight": 0.4 if user_input["priority"] == "fast" else 0.6,
        }

        return weights


# =========================================================
# Route Planning Agent
# =========================================================
class RouteAgent(BaseAgent):
    """
    Generates candidate routes (simulated).
    """

    def process(self, data):
        print(f"[{self.name}] Finding possible routes...")

        routes = [
            {"route": "Route A", "distance": 10, "time": 20},
            {"route": "Route B", "distance": 14, "time": 15},
            {"route": "Route C", "distance": 8, "time": 25},
        ]

        return routes


# =========================================================
# Cost Optimization Agent
# =========================================================
class CostAgent(BaseAgent):
    """
    Estimates travel cost based on distance.
    """

    def process(self, routes):
        print(f"[{self.name}] Estimating route costs...")

        for r in routes:
            r["cost"] = r["distance"] * 5  # simple cost model

        return routes


# =========================================================
# Time Scheduling Agent
# =========================================================
class TimeAgent(BaseAgent):
    """
    Evaluates time efficiency of routes.
    """

    def process(self, routes):
        print(f"[{self.name}] Evaluating travel times...")

        for r in routes:
            r["score_time"] = 1 / r["time"]

        return routes


# =========================================================
# Resource Management Agent
# =========================================================
class ResourceAgent(BaseAgent):
    """
    Validates feasibility of routes.
    """

    def process(self, routes):
        print(f"[{self.name}] Checking resource feasibility...")

        for r in routes:
            r["feasible"] = True  # assume feasible in simulation

        return routes


# =========================================================
# Decision Fusion Module
# =========================================================
class DecisionFusion:
    """
    Combines outputs from all agents and selects optimal route.
    """

    @staticmethod
    def select_best(routes, weights):
        print("[Fusion] Selecting optimal route...")

        best_score = -1
        best_route = None

        for r in routes:
            score = (
                weights["time_weight"] * (1 / r["time"])
                + weights["cost_weight"] * (1 / r["cost"])
            )

            if score > best_score:
                best_score = score
                best_route = r

        return best_route


# =========================================================
# Main Simulation Driver
# =========================================================
def run_planit():
    """
    Executes the full multi-agent planning pipeline.
    """

    print("\n🚀 Starting PlanIt Multi-Agent Simulation\n")

    # Step 1: User input
    user_input = {
        "source": "Location A",
        "destination": "Location B",
        "priority": "fast",  # change to 'cheap' to test
    }

    # Step 2: Initialize agents
    pref_agent = PreferenceAgent("PreferenceAgent")
    route_agent = RouteAgent("RouteAgent")
    cost_agent = CostAgent("CostAgent")
    time_agent = TimeAgent("TimeAgent")
    resource_agent = ResourceAgent("ResourceAgent")

    # Step 3: Agent pipeline
    weights = pref_agent.process(user_input)
    routes = route_agent.process(user_input)
    routes = cost_agent.process(routes)
    routes = time_agent.process(routes)
    routes = resource_agent.process(routes)

    # Step 4: Decision fusion
    best_route = DecisionFusion.select_best(routes, weights)

    # Step 5: Output result
    print("\n✅ OPTIMAL PLAN GENERATED:")
    print(best_route)


# =========================================================
# Program Entry Point
# =========================================================
if __name__ == "__main__":
    run_planit()