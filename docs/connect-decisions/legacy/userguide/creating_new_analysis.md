---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/creating_new_analysis.html
---

# Creating new analysis
<a name="creating_new_analysis"></a>

To create a new analysis, follow the below procedure.

**Note**
Granular access based on Location and Product is not supported in AWS Supply Chain Analytics.

1. On the Quick dashboard page, choose **New analysis**.

1. Choose **New dataset**

   The **Create a Dataset** page appears. You will see the AWS Supply Chain data lake as an existing dataset for you to pick. For example, ask-datalake-*your instance id*.
![Creating a dataset for AWS Supply Chain Analytics](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/Analytics_dataset.png)

1. Choose the data source.
**Note**
Select the blue Quick logo to navigate to the Quick menu to view the datasets or analyses.

1. Choose **Create dataset**.

1. Under **Schema:contain set of tables** drop-down, select one of the following data source names:
   + asc\_data\_<your instance id>: Contains datasets processed and transformed by AWS Supply Chain for use within the application. These can be used for creating dashboards and custom analyses. Examples include asc\_insights\_order\_insights and asc\_adp\_forecast. For more information on available datasets and their uses, see [Application datasets used in AWS Supply Chain Analytics](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/application_datasets.html).
   + asc\_custom\_data\_<your instance id>: Contains original, non-transformed data as provided. You can query these datasets to access and analyze your raw data directly and build dashboards out of them.

1. Under **Tables: contain the data you can visualize**, choose the dataset from the list of AWS Supply Chain datasets.
![Choosing a dataset category to create AWS Supply Chain Analytics dashboard](http://docs.aws.amazon.com/connect-decisions/legacy/userguide/images/Analytics_dataset1.png)

1. Choose **Select**.

1. Under **Finish dataset creation**, choose **Visualize**.

1. Under **Data**, choose the fields you want to visualize and choose **Publish**.

   The **Publish a dashboard** page appears.

1. Under **Publish new dashboard as**, enter a name for your dashboard.

1. Choose **Publish dashboard**.

   You will see the new dashboard created under **Dashboards** and a new analysis created under **Analyses**. For more information on using Dashboards or Analyses, see [Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html).
