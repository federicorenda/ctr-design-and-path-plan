from .heuristic import Heuristic


class SquareObstacleAvgPlusWeightedGoal(Heuristic):

    def __init__(self, goal_weight, this_obstacle_min, goal_dist):
        self.avg_obstacle_min = this_obstacle_min
        self.generation = 0
        self.goal_weight = goal_weight
        self.goal_dist = goal_dist
        self.cost = self._calculate_cost()

    def calculate_cost_from_parent(self, parent: 'SquareObstacleAvgPlusWeightedGoal'):
        if self.generation != 0:
            print(f"Cost already calculated. Do not run method twice.")
            return
        self.avg_obstacle_min = self._calculate_avg(parent.avg_obstacle_min,
                                                    parent.generation,
                                                    self.avg_obstacle_min)
        self.generation = parent.generation + 1
        self.cost = self._calculate_cost()

    def _calculate_cost(self):
        return self.goal_dist * self.goal_weight + self.avg_obstacle_min

    @staticmethod
    def _calculate_avg(parent_avg, parent_gen, this_obstacle_min):
        prior_sum = parent_gen * parent_avg
        weighted_min = (1 / this_obstacle_min)**2
        return (prior_sum + weighted_min) / (parent_gen + 1)

    def get_cost(self):
        return self.cost
