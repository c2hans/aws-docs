---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/connecting-sap-ecc.html
---

# Connecting to SAP ECC 6.0
<a name="connecting-sap-ecc"></a>

To extract your data from SAP ECC 6.0, follow the procedure below.

1. On the AWS Supply Chain dashboard, on the left navigation pane, choose **Data Lake**.

1. On the **Data lake** page, choose **Add New Source**.

   The **Select your supply chain data source** page appears.

1. Choose **SAP ECC**.

1. Under **SAP ECC Connection Details**, enter the following:
   + **Connection name** – Enter a name for your connection. Connection names can only contain letters, numbers, and dashes.
   + **Connection description** – Enter a description for your connection.

1. Under **Amazon S3 Bucket Billing**, review the Amazon S3 billing information, and then select **Acknowledge**.

1. Choose **Next**.

1. Under **Data Mapping**, choose **Get started**.

1.
**Note**
The required fields are already mapped. Perform this step only if you want to make specific changes to the default transformation recipe.

   On the **Mapping Recipe** page, you can view the default transformation recipe under **Field mappings**.

   Choose **Add mapping** to map any additional destination field. The **Required Destination Fields** are mandatory. Choose **Destination field** to add an additional custom destination field.

1.
**Note**
You can only use AWS Glue DataBrew to edit the recipes for transactional entities. Use AWS Supply Chain to download your recipes, and edit them in DataBrew. Then upload the recipes back into AWS Supply Chain. You can't use the AWS Supply Chain web application to edit the transactional data fields in a recipe.

    (Optional) Under **Recipe Actions**, you can do the following:
   + **Download recipe file** - Select **Download** to edit your recipe files offline with DataBrew.
   + **Upload recipe file** - Choose **browse files**, or move (drag and drop) your edited recipe files. Select **Confirm upload** to upload the edited recipe file and modify your data field mappings.
   + **Reset to default recipe** - Select **Yes, reset my recipe** to remove all your custom mappings and revert to the default recipe recommended by AWS Supply Chain.

1. To edit your source field mappings and validate your transformation recipe, you can upload sample data. On the **Mapping Recipe** page, under **Upload sample data**, choose **browse files**, or move (drag and drop) files. The sample data file must contain the required parameters and include the source field names.

1. Choose **Accept all and continue**.

1. Under **Review and confirm**, you can view the data connection summary. To edit your data field mapping, choose **Go back to Data Mapping**.

1. To review the Amazon S3 paths where you must upload your SAP source data for ingestion, choose **Confirm and configure data ingestion**. Alternatively, you can choose **Confirm and configure data ingestion later**. You can view the data ingestion information anytime. From the AWS Supply Chain dashboard, select **Connections**. Select the connection dataflow that you want to ingest data, choose the vertical ellipsis, and select **Ingestion setup**.

1. If you're not using the Amazon S3 API to ingest data, create the Amazon S3 path manually on the Amazon S3 console. For more information about how to create paths, see [Uploading data to an Amazon S3 bucket](manually-uploading-data.md).

1. Review the following table to map the AWS Supply Chain data entity with SAP source.
**Important**
On the **Amazon S3 path** page, you must upload the parent entity before the child entity. You can first upload all the parent entities and then upload all the child entities together.

- ** Company – [company](organization-company-entity.md) **
  - **SAP source:** 0COMP\_CODE\_TEXT
  - **Hierarchy:** Parent
  - **Data entity action:** Replace

- ** Geography – [geography](organization-geography-entity.md) **
  - **SAP source:** ADRC
  - **Hierarchy:** Parent
  - **Data entity action:** Replace

- ** Inventory – [inv\_level](inventory_mgmnt-inv-level-entity.md) **
  - **SAP source:** MARD / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** MCHB / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** VBBE / **Hierarchy:** Child / **Data entity action:** Update

- ** Inventory – [inv\_policy](planning-inv-policy-entity.md) **
  - **SAP source:** MARC / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** 0MATERIAL\_ATTR / **Hierarchy:** Child / **Data entity action:** Update

- ** Outbound – [outbound\_order\_line](outbound-fulfillment-order-line-entity.md) **
  - **SAP source:** 2LIS\_11\_VAITM / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** 0BP\_DEF\_ADDRESS\_ATTR / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** 0MATERIAL\_ATTR / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** 2LIS\_11\_VAHDR / **Hierarchy:** Child / **Data entity action:** Update

- ** Outbound – [outbound\_shipment](outbound-fulfillment-shipment-entity.md) **
  - **SAP source:** 2LIS\_08TRTLP / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** 2LIS\_08TRFKP / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** 2LIS\_08TRTK / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** 2LIS\_12\_VCITM / **Hierarchy:** Child / **Data entity action:** Update

- ** Product – [product](product-product-entity.md) **
  - **SAP source:** 0MATERIAL\_ATTR / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** 0MATERIAL\_TEXT / **Hierarchy:** Child / **Data entity action:** Update

- **Product – [product\_hierarchy](product-hierarchy-entity.md)**
  - **SAP source:** T179
  - **Hierarchy:** Parent
  - **Data entity action:** Replace

- **Purchase order – [inbound\_order](replenishment-inbound-order-entity.md)**
  - **SAP source:** 2LIS\_02\_HDR / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** CDHDR / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** EKKO / **Hierarchy:** Child / **Data entity action:** Update

- **Purchase order – [inbound\_order\_line](replenishment-inbound-order-line-entity.md)**
  - **SAP source:** 2LIS\_02\_ITM / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** 0MATERIAL\_ATTR / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** 2LIS\_03\_BF / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** EKPO / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** LIPS / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** LIKP / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** INB-SHIPMENT / **Hierarchy:** Child / **Data entity action:** Update

- **Purchase order – [inbound\_order\_line\_schedule](replenishment-inbound-order-line-schedule-entity.md)**
  - **SAP source:** 2LIS\_02\_SCL / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** 2LIS\_02\_SCN / **Hierarchy:** Child / **Data entity action:** Update

- **Production order – [inbound\_order](replenishment-inbound-order-entity.md)**
  - **SAP source:** 2LIS\_04\_P\_MATNR
  - **Hierarchy:** Parent
  - **Data entity action:** Update

- **Production order – [inbound\_order\_line](replenishment-inbound-order-line-entity.md)**
  - **SAP source:** 2LIS\_04\_P\_MATNR / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** 0CO\_PC\_ACT\_05 / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** 0MATERIAL\_ATTR / **Hierarchy:** Child / **Data entity action:** Update

- **Reference – [reference\_field](reference-fields-entity.md)**
  - **SAP source:** 0PURCH\_ORG\_TEXT / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** MDRP\_NODTT / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** T005T / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** T141T / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** T173T / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** T179T / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** T370U / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** T618T / **Hierarchy:** Parent / **Data entity action:** Update

- **Shipment – [shipment](replenishment-shipment-entity.md)**
  - **SAP source:** INB-SHIPMENT / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** EQUI / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** LIKP / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** LIPS / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** 0MATERIAL\_TEXT / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** 0MAT\_VEND\_ATTR / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** 0MATERIAL\_ATTR / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** EKPO / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** T001W / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** ADRC / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** 0VENDOR\_ATTR / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** BUT021\_FS / **Hierarchy:** Parent / **Data entity action:** Replace

- **Site – [site](network-site-entity.md)**
  - **SAP source:** T001W / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** ADRC / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** GEOLOC / **Hierarchy:** Child / **Data entity action:** Update

- **Trading partner – [trading\_partner](organization-trading-partner-entity.md)**
  - **SAP source:** 0BPARTNER\_ATTR / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** 0BPARTNER\_TEXT / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** 0VENDOR\_ATTR / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** 0CUSTOMER\_ATTR / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** 0BP\_DEF\_ADDRESS\_ATTR / **Hierarchy:** Child / **Data entity action:** Update

- **Transfer order – [inbound\_order\_line](replenishment-inbound-order-line-entity.md)**
  - **SAP source:** 2LIS\_03\_BF / **Hierarchy:** Parent / **Data entity action:** Update
  - **SAP source:** 0MATERIAL\_ATTR / **Hierarchy:** Child / **Data entity action:** Update

- **Transportation – [transportation\_lane](network-transporation-lane-entity.md)**
  - **SAP source:** TVRO / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** TVRAB / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** VALW / **Hierarchy:** Child / **Data entity action:** Update

- **Vendor management – [vendor\_lead\_time](vendor-management-lead-time-entity.md)**
  - **SAP source:** EINA / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** EINE / **Hierarchy:** Child / **Data entity action:** Update
  - **SAP source:** 0MATERIAL\_ATTR / **Hierarchy:** Child / **Data entity action:** Update

- **Vendor management – [vendor\_product](vendor-management-product-entity.md)**
  - **SAP source:** EINA / **Hierarchy:** Parent / **Data entity action:** Replace
  - **SAP source:** 0MATERIAL\_ATTR / **Hierarchy:** Child / **Data entity action:** Update

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
