def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices



products = ["mobile", "tablet", "laptop", "mobile", "computer", "mobile"]
target = "mobile"
target2 = 'camara'
result = linearSearchProduct(products, target)
print(result)