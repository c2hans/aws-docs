---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/dataset-requirements.html
---

# Dataset requirements
<a name="dataset-requirements"></a>

The following are important dataset requirements:
+ Default roles automatically include access to all required datasets.
+ Custom roles must be granted access to seven essential datasets: asc\_adp\_dp\_segmentation, asc\_adp\_forecast, asc\_adp\_planning\_cycle\_accuracy, outbound\_order\_line, product, product\_alternate, and supplementary\_time\_series.
+ Access to "asc\_adp\_dp\_segmentation" is specifically required for demand pattern and recommendation functionality.
