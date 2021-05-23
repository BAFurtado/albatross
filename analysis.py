# import model
#
# # Wanted outputs
# # 1. Share of advertisers
# # 2. Users satisfaction over time
# # 3. Concentration of pages visited
# # 4. Concentration of advertisers
# # 5. Diversity of pages visited (within platforms)
#
# #Overall, Time series
# #1. Platform v Advertisers
# #2. Platform v Visits
# print(dir(model))
# prs = model.to_dict_from_module()
# # TODO include scenarios.
# m1 = model.AlbatrossModel(prs)
# for step in range(prs['step_count']):
#     print(f"Starting step {step}")
#     m1.step()
