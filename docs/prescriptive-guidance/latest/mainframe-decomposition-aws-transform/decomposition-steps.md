---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/decomposition-steps.html
---

# Decomposing the code
<a name="decomposition-steps"></a>

## Prerequisites
<a name="prerequisites"></a>

This demonstration uses the [CardDemo mainframe credit card management application](https://github.com/aws-samples/aws-mainframe-modernization-carddemo). Before you start the decomposition, follow these steps:

1. Input the application code into AWS Transform.

1. Complete the analysis phase.

1. Generate technical documentation and review documentation results.

For instructions, see steps 1-8 in the [Transformation of mainframe applications](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html) section of the AWS Transform documentation.

For the following steps, use these options on the AWS Transform console:
+ Use **Create domain** to create domains by selecting components and identifying them as seeds. As discussed in the [previous section](seeds.md), seeds are key elements that help identify and group related components into domains.
+ Use the **Actions** menu to create domains, edit domains, remove domains, import domain files, download domain files, configure decomposition, and update dependencies files.

## Step 1: Identify seeds
<a name="identify-seeds"></a>

In this step, you create domains based on the [decomposition strategy](decomposition-overview.md) you've decided to use. The following example assumes that you're using the strangler fig pattern. The seeds for decomposing the CardDemo application are based on transaction naming standards. The application is decomposed into several online domains that manage different functions in the application, and the batch processing is assigned to a separate domain. The seeds used for different domains are as follows.
+ Domain 1: Account Management
  + `CAVW` – Account View
  + `CAUP` – Account Update
+ Domain 2: Card Management
  + `CCLI` – CC List
  + `CCDL` – CC View
  + `CCUP` – CC Update
+ Domain 3: Transactions Management
  + `CT00` – Transaction List
  + `CT01` – Transaction View
  + `CT02` – Transaction Add
  + `CR00` – Transaction Reports
+ Domain 4: Bill Pay (Pay Balance)
  + `CB00` – Bill Payment
+ Domain 5: Administration Menu
  + `CA00` – Administration Menu
  + `CU00 `– List User
  + `CU01` – Add User
  + `CU02` – Update User
  + `CU03` – Delete User
+ Domain 6: CardDemo Batch Processing
  + `*.JCL` – All JCL files that handle maintenance

## Step 2: Create domains
<a name="create-domains"></a>

Choose the **Create domain** command to create the first domain (Account Management).

Provide a unique name and a meaningful description for the domain. The list of files can be ordered by name, type, seeds (if they were identified previously), or cyclomatic complexity.

For the Account Management domain, you can identify seeds based on transactions. Select files that have a type of **TRANSACTION**, and select the transactions **CAUP** and **CAVW**, as shown in the following screen illustration. Choose **Mark as seed** to identify these elements as seeds for the Account Management domain. Choose **Create** to create the domain.

![Identifying seeds for a domain in mainframe decomposition.](https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/images/guide-img/b2468f31-0c9f-4fc4-9a0f-816b3ed5739c/images/78af476c-4c2b-4d9c-888c-815c0b6a9897.png)

Repeat this process for the five remaining domains identified in step 1, by choosing **Create domain** from the **Actions** menu. The next screen provides a tabular view of the domains, the number of files you selected for each domain, and the number of seeds, as shown in the following illustration.

![Tabular view of a domain in mainframe decomposition.](https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/images/guide-img/b2468f31-0c9f-4fc4-9a0f-816b3ed5739c/images/6eea8992-7d41-4793-937a-dd69d75fcddb.png)

## Step 3: Configure decomposition and enable seed augmentation
<a name="configure-decomposition"></a>

After you define your domains and select seeds for decomposition, choose **Configure decomposition**. The **Domain configuration** tab, as shown in the next illustration, displays the threshold configuration that can be set at the domain level, to provide flexible domain sizes across different parts of the project.

![Domain size thresholds in mainframe decomposition.](https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/images/guide-img/b2468f31-0c9f-4fc4-9a0f-816b3ed5739c/images/e2b6201f-b718-4a5a-b096-a062d87e79d2.png)

## Step 4: Make additional changes before decomposition
<a name="make-changes"></a>

You can export the domains as a JSON or CSV file, modify it, and upload it back to AWS Transform. The import/export option provides the flexibility for you to further define and modify domains. In addition, you can download, modify, and upload the dependencies file and then choose **Decompose**.

## Step 5: Decompose into domains
<a name="decompose-domains"></a>

When you choose **Decompose**, the **View decomposition results** screen provides the results of the decomposition in table view, as shown in the following illustration. It displays the domain name, description, file percent (percentage of number of files compared with total files), number of files, number of seeds, and lines of code for each domain.

![Tabular view of decomposition results in mainframe decomposition.](https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/images/guide-img/b2468f31-0c9f-4fc4-9a0f-816b3ed5739c/images/0357cf73-aed8-4634-bc20-ce7ced1313f6.png)

When you choose a domain, the screen also displays the details of all files that have been identified as part of that domain, as shown in the following illustration.

![Drilling down to see domain-specific information in mainframe decomposition.](https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/images/guide-img/b2468f31-0c9f-4fc4-9a0f-816b3ed5739c/images/f667a024-2be6-4689-902b-4c4e021502ba.png)

You can also choose the graph view to see graphical dependencies or domains at the domain level.

Based on the results of the decomposition, you can make additional changes to the domains and seeds, and decompose the domain again. You can use the dependencies file to download dependencies from the AWS Transform analysis, update them, and upload the file again. AWS Transform will display the dependencies based on the updated information.

When you are satisfied with the decomposition analysis, you can send this information to AWS Transform to complete the domain-based decomposition and create initial wave plans. After decomposition is complete, the dashboard, shown in the following screen illustration, displays a summary of decomposition results. It shows the number of files by domain along with the percentage of files in each domain.

![AWS Transform dashboard with decomposition results.](https://docs.aws.amazon.com/prescriptive-guidance/latest/mainframe-decomposition-aws-transform/images/guide-img/b2468f31-0c9f-4fc4-9a0f-816b3ed5739c/images/63e6fa31-9394-4005-add0-e6de93a3b3ad.png)
