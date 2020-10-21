# Inferring a Context Free Grammar

This is a first attempt at creating a <b>very</b> rudimentary machine learning project capable of inferring a context free grammar that is able to differentiate tokens. Specifically, VIN(s), phone numbers, dates, email addresses and names (which is basically a catch all). While much of this could be accomplished algorithmically with regular expressions the goal is to create an unsupervised learning mechanism able to infer the production rules when exposed to a sufficient corpus of new symbols. This can be used for content identification, extraction and classification. It is not intended for use as a validator but for candidate selection or elimination.

- grammer.v1.joblib initial version
- grammar.v2.joblib adds email support 

Thanks to [vingenerator.org](https://vingenerator.org/brand) for providing an excellent VIN generator resource 

## Reference
- [Run Local](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=linux%2Ccsharp%2Cbash#v2)
- [Python Function Developer Reference](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
