---
source_url: https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/post-deployment-tasks.html
---

# Post-deployment tasks
<a name="post-deployment-tasks"></a>

 After the stack has successfully deployed, complete these post-deployment tasks.

## Post-deployment overview
<a name="post-deployment-overview"></a>

 Use the following steps to deploy this guidance on AWS. For detailed instructions, follow the links for each step.

[Step 1. Confirm crawler completion](#post-deployment-tasks)

[Step 2. Confirm Omics resource creation](#step-2.-confirm-omics-resource-creation)

[Step 3. Launch the QuickSight resource stack](#step-3.-launch-the-quicksight-stack)

[Step 4. Explore the data using QuickSight](#step-4.-explore-the-data-using-quicksight)

[Step 5. Make Amazon Omics data available in Athena](#step-5.-make-amazon-omics-data-available-in-athena)

[Step 6. Query data in the data lake](#step-6.-query-data-in-the-data-lake)

## Step 1. Confirm crawler completion
<a name="step-1.-confirm-crawler-completion"></a>

**Note**
The Parquet version of the datasets are copied into the data lake bucket after the guidance is set up so that running these AWS Glue jobs is optional. We run the AWS Glue crawlers on these datasets automatically during setup of the guidance to create the tables in the data catalog. The AWS Glue jobs are provided for modification and reference.

 The AWS Glue crawlers are launched after deployment completes. You must confirm that all crawlers are complete before proceeding with further steps to explore the data using QuickSight or Jupyter.

 Use the following steps to verify the crawler status:

1.  Sign in to the [AWS Glue console](https://console.aws.amazon.com/glue/home).

1.  Select **Crawlers** on the left navigation pane.

1.  Wait for all crawlers to show status as **READY**, and the **Tables added** column to each be **1 or larger**.

## Step 2. Confirm Omics resource creation
<a name="step-2.-confirm-omics-resource-creation"></a>

The Amazon Omics Reference, Variant, and Annotation stores are created. 1000 Genomes, the example VCF, and ClinVar Annotation data are loaded into the stores once the solution is deployed.

Follow these steps to verify resource creation:

1. Sign into the [Amazon Omics console](https://us-east-1.console.aws.amazon.com/omics/home)

1. Select **Storage > Reference store** in the left navigation page.

1. Verify the presence of **hg38** under **Reference Genomes** with Import status set to **Active**.

1. Select **Analytics > Variant stores** in the left navigation page.

1. Verify that Variant store with name **omicsvariantstore** has status set to **Active**.

1. Choose **omicsvariantstore** and verify that there are two **Job ID**s with **Import** status set to **Completed**. These correspond to the import of the 1000 Genomes VCF and the example VCF.

1. Select **Analytics > Annotation** stores in the left navigation page.

1. Verify that Annotation store with the name **omicsannotationstore** has status set to **Active**.

1. Choose **omicsannotationstore** and verify that there is a **Job ID** with **Import** status set to **Completed**. This corresponds to the import of the ClinVar VCF.

## Step 3. Launch the QuickSight stack
<a name="step-3.-launch-the-quicksight-stack"></a>

**Note**
To create Quick resources, the AWS CloudFormation stack requires the user to input their QuickSight User ID. This User ID can be retrieved from Quick through the following steps:
 Sign in to Quick.
 Select the dropdown menu in the upper right of the display.
 Choose the menu option containing your username.
 In the resulting **Account info** screen, copy the entire text under the **Username** field.

 To assist the user in exploring the use of Quick to analyze multi-omics data, the guidance provides a CloudFormation template that automatically creates the necessary QuickSight data source and dataset, as well as adds a policy to the QuickSight service IAM role to grant it permissions to access the relevant data resources.

 Use the following steps to create Quick resources for this guidance:

1.  Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1.  Select **Stacks** in the left navigation pane, then select the **Imaging** stack.

1.  Select the **Outputs** tab, then select the link shown in the **CreateQuicksightLink** output. This opens the CloudFormation **Create Stack** wizard with the stack name and project name pre-filled.

   1.  In the **QuicksightUserId** parameter field, paste in your username information from QuickSight.

   1.  If during the setup process of Quick, you selected an alternate IAM role for the QuickSight service, you must update the **QuicksightServiceRoleName** with the correct name of the IAM role being used by QuickSight.

   1.  Check the box to acknowledge that the template will create AWS Identity and Access Management (IAM) resources.

1.  Choose **Create stack** to deploy the stack.

1. You can view the status of the stack in the AWS CloudFormation Console in the **Status** column. You should see a status of CREATE\_COMPLETE in approximately 1 minute.

## Step 4. Explore the data using QuickSight
<a name="step-4.-explore-the-data-using-quicksight"></a>

Once the QuickSight template has completed, you can create a QuickSight Analysis to explore the data graphically with interactive filters. The steps below are recommended; however, feel free to follow your own path when exploring this data.

1.  Open the QuickSight console from the AWS Management Console by searching for **QuickSight**.

1.  In the **Datasets** tab, locate the new dataset with your selected project name and choose it to open.

1.  Choose **Create analysis**.

1.  Your analysis will begin with a pre-selected AutoGraph visual. Change this to a **Horizontal Bar Chart** by selecting the appropriate icon in the **Visual types** panel.

1.  From the **Fields list**, drag the **age\_at\_dx\_numeric** field to the **Y axis** field well at the top of the screen. Your visual will now show **Count of Records by Age\_at\_dx\_numeric**.

1. The visual by default will zoom into the data, which you can navigate using the vertical scroll bar in the visual tile.

1.  To view the entire data set, with the visual selected, choose the **Format visual** gear icon in the small context menu that appears to the upper right of the visual. Then, expand the **Y-axis** settings and uncheck **Show data zoom**.

1. Next, we will add a second visual to look at an additional field.

1.  Choose the **\+ Add** button in the upper-left and select **Add visual**.

1.  From the **Visual types** panel, choose the **Heat map** visual type.

1.  Drag the **egfr\_mutation\_status** field from the **Fields list** to the **Rows** field well, and drag the **eml4\_alk\_translocation\_status** field to the **Columns** field well.

1. The visual now shows a heat map of the number of patients who have had their tumors tested for EML4-ALK translocation and EGFR mutation status. Because there are a substantial number of patients without test results, let’s add some filters to the data set to clean this up.

1.  Select the **Filter tab** and ensure that you have the newly created heat map visual selected.

1.  Choose the **\+** button in the **Filters** section to add a new filter and select **eml4\_alk\_translocation\_status** as the field to filter.

1.  Choose the newly created filter and change the following settings:

   1.  Change the **Only this visual** dropdown to **All visuals of this dataset**.

   1.  In the **Include** list, unselect the **[Not Available]** and **[Unknown]** options.

1.  Choose **Apply** to see the effect of the new filter, and then choose **Close**.

1.  Repeat steps 11 through 13, but this time select the **egfr\_mutation\_status** field.

1. Next, create a pivot table that shows the number of data records available for each category of patients in our filtered cohort.

1.  Choose the **\+ Add** button in the upper-left and select **Add visual**.

1.  From the **Visual types** panel, choose the **Pivot table** visual type.

1.  Drag both the **egfr\_mutation\_status** and **eml4\_alk\_translocation\_status** fields from the **Fields list** to the **Columns** fields well.

1.  In the **Values** fields well, change it to “Row” mode by selecting **Row**, then drag all of the **num\_...\_records** fields into the **Values** field well.

1.  For each entry in the **Values** field well, change the **Aggregate** function from **Sum** to **Count** by choosing the dropdown arrow, then selecting **Count** from the **Aggregate** menu.

1. Finally, create a table listing the patient IDs that are in the current analysis. This can be exported as a CSV file to create a cohort for further analysis.

1.  Choose the **\+ Add** button in the upper-left and select **Add visual**.

1.  From the **Visual types** panel, choose the **Table** visual type.

1.  Drag the **bcr\_patient\_barcode** field into the **Value** field well. You can add additional fields such as those we have used in the filters or other visuals.

1.  To export the list of patients as a CSV file, in the small context menu that appears to the upper right of the visual, choose the **Menu options** (**…**) icon, then select **Export to CSV.**

## Step 5. Make Amazon Omics data available in Athena and SageMaker Notebook
<a name="step-5.-make-amazon-omics-data-available-in-athena"></a>

 Once the Omics resources are created and verified, you can make the data in the Omics Variant Store and Omics Annotation Store available in Athena for querying through AWS Lake Formation.

1. Navigate to AWS Lake Formation, you should see the variant store and annotation store resource shares listed under **Data catalog > Tables** with the names for the Omics stores. In this case, **omicsvariantstore** and **omicsannotationstore**.

1. Select **omicsvariantstore,** choose **Actions** and choose **Create resource link**. Give the resource link a name, such as {{variants}}. This will be the table name that will show up in Athena. This table can be added to the existing solution database `>genomicsanalysis`. Once created, repeat the process for the annotation store** omicsannotationstore**and give it a name, such as {{ annotations}}.

1. Once resource links are created, select the newly created table {{variants}} under **Tables**, choose **Actions** and select **Grant on target**. Select the user and role that you want to allow access.
**Note**
 To allow query from the SageMaker Notebook created as part of the solution, select the IAM Role created for the SageMaker notebook instance. To identify the IAM Role name, navigate to AWS Identity and Access Management (IAM) console, select **Roles** under **Access management** in the left navigation page, search for **RunbookRole**. You should get a result with the full name of the IAM Role used by the SageMaker notebook instance.

1. Next, under **LF-Tags** or **catalog resources**, select **Named data catalog resources** and choose the resource link created for the database, such as `{{<account-id>}}-{{<variant-store-id>}}-variant`. Select **All tables**. Under **Table permissions**, check the **Select** and **Describe** box under **Table permissions and Grantable permissions**. Select **All data access** under **Data permissions** and choose **Grant**. Repeat the process for the {{ annotations}} table.

1. After the previous step completes successfully, navigate to Amazon Athena in the console, select AwsDataCatalog under Data source and genomicsanalysis under **Database**. Verify that you are able to see the newly created tables {{variants}} and {{ annotations}} under **Tables and views**. Also verify that you have selected **Workgroup genomicsanalysis-{{aws-region}}**. You are now ready to run a query against all the data in these databases.

## Step 6. Query data in the data lake
<a name="step-6.-query-data-in-the-data-lake"></a>

**Note**
An [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) notebook instance is provisioned with an example Jupyter notebook that demonstrates how to work with data in a genomics data lake. The notebook uses [Amazon Athena](https://aws.amazon.com/athena/) to identify genomic variants related to drug response for a given cohort of individuals. The following query is run against data in the data lake using the PyAthena driver to 1) filter by samples in a subpopulation, 2) aggregate variant frequencies for the subpopulation-of-interest, 3) join on the ClinVar dataset, 4) filter by variants that have been implicated in drug-response, 5) order by highest frequency variants.

 You can generate an example cohort creation and drug response by running each step in the provided demonstration Jupyter Notebooks.

### Option 1: Use the provided Jupyter Notebooks
<a name="option-1-use-the-provided-jupyter-notebooks"></a>

 Use the following steps to run the notebook:

1.  Sign in to the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/home).

1.  Select **Notebook Instances** under the Notebook category on the left pane.

1.  Select your notebook instance and choose **Open Jupyter**.

1.  To explore cohort creation, clinical dataset enrichment, and imaging visualization, select **cohort-creation.ipynb**.

1.  Run each step in the notebook.

1.  To explore the creation of a drug response report, in the main Jupyter window, select **runbook.ipynb**.

1.  Run each step in the notebook.

### Option 2: Run the drug response report query in the Amazon Athena console
<a name="option-2-run-the-drug-response-report-query-in-the-amazon-athena-console"></a>

 Use the following setups to run the query in the Amazon Athena console:

1.  Sign in to the [Amazon Athena console](https://console.aws.amazon.com/athena/home).

1.  Under **Data Source** select the **AwsDataCatalog** data source on the left pane.

1.  Under **Database** select the **genomicsanalysis** database on the left pane.

1.  In the query window paste the query below.

1.  Select **Run Query**.

   ```
   SELECT  count(*)/cast(numsamples AS DOUBLE) AS genotypefrequency
       ,cv.attributes['RS'] as rs_id
       ,cv.attributes['CLNDN'] as clinvar_disease_name
       ,cv.attributes['CLNSIG'] as clinical_significance
       ,sv.contigname
       ,sv.start
       ,sv."end"
       ,sv.referenceallele
       ,sv.alternatealleles
       ,sv.calls
           FROM {variant_table_name} sv
           CROSS JOIN
               (SELECT count(1) AS numsamples
               FROM
                   (SELECT DISTINCT vs.sampleid
                   FROM {variant_table_name} vs
                   WHERE vs.sampleid LIKE 'NA12%'))
           JOIN {annotation_table_name} cv
           ON sv.contigname = cv.contigname
               AND sv.start = cv.start
               AND sv."end" = cv."end"
               AND sv.referenceallele = cv.referenceallele
               AND sv.alternatealleles = cv.alternatealleles
               AND cv.attributes['CLNSIG'] LIKE '%response%'
               AND sv.sampleid LIKE 'NA12%'
           GROUP BY  sv.contigname
                     ,sv.start
                     ,sv."end"
                     ,sv.referenceallele
                     ,sv.alternatealleles
                     ,sv.calls
                     ,cv.attributes['RS']
                     ,cv.attributes['CLNDN']
                     ,cv.attributes['CLNSIG']
                     ,numsamples
           ORDER BY genotypefrequency DESC LIMIT 50
   ```
