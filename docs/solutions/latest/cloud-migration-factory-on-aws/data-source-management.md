---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/data-source-management.html
---

# Data source management
<a name="data-source-management"></a>

In addition to automated wave planning, the Wave Planning Manager (WPM) module also enables many-to-many relationships during import. With this capability, applications can be deployed to many servers and a server can support many applications.

The import process is different, and requires the creation of a data source.

## Data sources
<a name="data-source-management-data-sources"></a>

A data source is a configured input mechanism in the Wave Planning Module (WPM) that defines where your migration data comes from, and how your input file maps to pre-existing assets in CMF.

### To create a new data source
<a name="to-create-a-new-data-source"></a>

1. In the navigation menu, select **Wave Planning** > **Data source**

1. The table shows a list of data sources previously created. Choose **Add**

1. Fill out the data source general settings and upload the input file containing data you wish to import

   1. Once you upload your file, the choose entities screen will appear. Select the CMF entities the data in the file maps to in the drop-down. If you’ve uploaded an excel file, you can map multiple sheets to different CMF entities. ie Sheet 1 could contain all your servers, Sheet 2 could contain all your applications, etc.

1. The next step involves mapping headers from your input file to schema attributes for each entity you selected in the previous step. Begin by selecting the sheet you wish to map, and the entity you wish to map to. You can then map each header in your source file to an schema attribute by selecting from the drop-down options

   1. For more details on how header mapping works, see [header mapping](#data-source-management-header-mapping)

1. The next step is the review screen. Here you can review all the input headers and how they map to each entity in CMF. In addition you can also see any schema attributes which will be automatically created alongside this data source. **Note** once you proceed past this step the data source and schema attributes will be created in CMF

1. The final screen provides an opportunity to do a data import dry-run, to test and verify what will happen when your newly created data source is used during an actual data import. No actual data will be imported into CMF during this step. You can see what entities would have been created, along with any validation errors/warnings CMF would have encountered if this was a proper data import. You can either go back to previous steps in the wizard to make further updates to the data source if there are errors, or save & close the wizard. Your data source will now be available for other users to use for actual data import jobs.

   1. If you encounter validation errors regarding attributes that don’t meet input requirements, you can update the attribute in your input file to pass validation & re-import. Alternatively if this is not possible, you can update the attribute constraints in CMF (**Administration** > **Attributes** > {Schema Name} > {Attribute Name} > **Edit** > **Input validation**). **Note** that if you do this for pre-existing attributes, other functionality in CMF may be affected.

### Header mapping
<a name="data-source-management-header-mapping"></a>

One of the key features of data sources is header mapping. By leveraging header mapping, you can bring your own file with your own header names and dynamically map them to related CMF entity schema attributes. Below is an overview of some of the features you may encounter during header mapping.

#### Auto map headers
<a name="data-source-management-auto-map-headers"></a>

**Note**
This feature requires Generative AI. See the [Prerequisites](prereqs.md) section of the deployment guide for more information on whether it is enabled.

When you select a new sheet from your input file to import, an Auto map headers button will appear.

WPM will leverage Generative AI to attempt to automatically map your input file headers to entity schema attributes. If it does not find a match, it may also recommend a new schema attribute name which can be automatically created in the entity alongside the data source. If it does make a recommendation, you’ll see 🤖 (NEW) appended to the end

![header mapping](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/header-mapping.png)

**Warning**
Please be aware the generative AI capabilities of header mapping may not always be 100% accurate. Results should be reviewed and validated by users.

#### Auto create schema attributes
<a name="data-source-management-auto-create-attributes"></a>

Available entity attributes are listed in the drop-down when mapping each input header. If an exact mapping is not found, one of the options will be the header name with (NEW) appended to the end of it. This option is available if you have a custom attribute not currently in the CMF entity you are mapping. If you select this option, the attribute will be automatically created in the linked entity at the same time as the data source.

## Data import
<a name="data-source-management-data-import"></a>

Once a data source is created, resources can then be imported into CMF.

### To import data
<a name="to-import-data"></a>

1. In the menu, select **Wave Planning** > **Import**.

1. The table shows a list of data import jobs. Choose **Add**.

1. Select your data source from the list of data sources. Choose **Next**.

1. Choose **Choose file**.

1. Locate the local XLSX or CSV file containing your resources. This file must share column headings as that defined in the data source. If it is a XLSX file, it also must share the same sheet names. Choose **Next**.

1. Choose the **Validation Issues** tab to review any validations warnings or errors. If updates are required to your import file, choose **Cancel**.

1. Choose the **Validated Entities** tab to review the resources that will be created and updated. If updates are required to your import file, choose **Cancel**. Otherwise, choose **Next**.

1. Review a summary of the job. When ready, choose **Import Data**.

You will be redirected to the Data import page. A new job will be created with the **Pending** status.

### Data import job statuses
<a name="data-import-job-statuses"></a>

To support a large number of resources in a data import, it is an asynchronous process. The status of the job can be monitored on the **Wave Planning** > **Import** page. The following table details the statuses for a job.

| Status | Definition |
| --- | --- |
| Pending | A job request has been made but the server has not yet allocated resources to process. |
| Processing | The server is currently processing the import. |
| Completed | The server has completed the import. Resources were successfully imported. |
| Failed | The server has completed the import. At least one resource was not successfully imported. |

### To monitor the status of an import job
<a name="to-monitor-the-status-of-an-import-job"></a>

1. In the menu, select **Wave Planning** > **Import**.

1. From the list of Data import jobs, locate the job you want to monitor. Inspect the **Status** column. Wait until the status shows **Completed** or **Failed**.

1. Select the import job to monitor by choosing the **Upload ID**.

1. Assuming the job was in a **Completed** state, two tabs will be shown: **Summary** and **Processed Items**. If your job is in a **Failed** state, see the following **To troubleshoot a failed import** guide.

1. Choose the **Summary** tab for an overview of the job.

1. Choose the **Processed Items** tab to see a list of all resources that were successfully created or updated.

![import job details](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/import-job-details.png)

### To troubleshoot a failed import
<a name="to-troubleshoot-a-failed-import"></a>

1. In the menu, select **Wave Planning** > **Import**.

1. From the list of Data import jobs, locate the **Failed** job. Select the **Upload ID**.

1. Choose the **Summary** tab for an overview of the job.

1. Choose the **Processed Items** tab to see a list of all resources that were successfully created or updated.

1. Choose the **Failed Import Items** tab to see a list of all resources that were not successfully created or updated. The table will detail the error for each entity.

![import job details failures](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/import-job-details-failures.png)

### Required attributes vs Optional attributes
<a name="required-attributes-vs-optional-attributes"></a>

We have removed the requirement for certain server fields such as subnet IDs, AWS Region, and AWS Account ID during WPM import, as this information may not be available during the initial wave planning phase. However, these fields are essential for pipeline execution and migration activities. Users must ensure these required attributes are added and properly configured before:

1. Executing any CMF pipeline

1. Performing actual migration activities
