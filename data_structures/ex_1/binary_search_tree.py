class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    answer = []
    cb(self.value)
    if self.left:
      newtree = self.left
      if newtree.left or newtree.right:
        self.left.depth_first_for_each(cb)
      else:
        cb(self.left.value)
    if self.right:
      newtree = self.right
      if newtree.left or newtree.right:
        self.right.depth_first_for_each(cb)
      else:
        cb(self.right.value)
    return answer

  def breadth_first_for_each(self, cb):
    root = self
    answer = []
    queue = []
    def _breadth(node):
      if len(queue) > 0:
            del queue[0]
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
      while len(queue) > 0:
        for node in queue:
          cb(node.value) 
          _breadth(node)
    cb(root.value)
    _breadth(root)
    return answer
   

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
