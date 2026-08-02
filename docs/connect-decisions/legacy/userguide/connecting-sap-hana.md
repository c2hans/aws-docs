---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/connecting-sap-hana.html
---

# Connecting to S/4 HANA
<a name="connecting-sap-hana"></a>

Before you can connect to your S/4 HANA data source, you must complete the following prerequisites. After that, AWS Supply Chain automatically creates the Amazon S3 paths and ingests data from the SAP source tables.

## Prerequisites to connect to S/4 HANA
<a name="prerequisites-s4hana"></a>

To connect to S/4 HANA data source, the following prerequisites must be completed before ingesting data.

1. Configure your SAP S/4 HANA system to turn on ODP-based data extraction through the SAP OData connector for Amazon AppFlow. For more information, see [SAP OData connector for Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/sapodata.html).

1. Configure your SAP data sources or extractors, and generate ODP based OData services for AWS Supply Chain to connect and extract information. For more information, see [SAP data sources](#s4-datasources).

1. Configure your SAP system with one of the following types of authentication:
   + Basic
   + OAuth

1. Configure security roles in the SAP system to turn on data extraction.

1. Set up network connectivity to SAP S/4 HANA. If your SAP instance is in a secure VPN and you can't open a port for AWS Supply Chain to connect, we recommend that you use AWS PrivateLink. To manually setup AWS PrivateLink, see [AWS for SAP](https://aws.amazon.com/blogs/awsforsap/share-sap-odata-services-securely-through-aws-privatelink-and-the-amazon-appflow-sap-connector/) and to automatically setup using CloudFormation, see [CloudFormation](https://github.com/aws-cloudformation/aws-cloudformation-templates/tree/main/AWSSupplyChain/SapPrivateLink).

## Configuring S/4 HANA connection
<a name="connecting-s4hana"></a>

To ingest data from an SAP S/4HANA data source, follow the procedure below.

1. On the AWS Supply Chain dashboard, on the left navigation pane, choose **Data Lake**.

1. On the **Data lake** page, choose **Add New Source**.

   The **Select your supply chain data source** page appears.

1. Choose **SAP S/4HANA**.

1. Choose **Next**.

1. Under ** SAP S/4HANA Connection Details**, enter the following:
   + **Connection name** – Enter a name for this connection.
   + (Optional) **Connection description** – Enter a name for this connection.
   + **Use Existing AppFlow Connector** – Choose **Yes** to use an existing AppFlow connector.
   + **Application Host URL** – Enter the SAP account's URL.
   + **Application Service Path** – Enter the SAP application service path.
   + **Port Number** – Enter the SAP port number.
   + **Client Number** – Enter the SAP client number.
   + **Logon Language** – Enter the SAP language code. For example, EN for English.
   + **PrivateLink** – Choose **Enabled** to enable a private connection between the SAP server and your AWS account hosting AWS Supply Chain.
   + **Username** – Enter the username of the SAP account.
   + **Password** – Enter the password of the SAP account.
**Note**
Amazon AppFlow uses the SAP **Username** and **Password** provided by you to connect to SAP.

1. Choose **Connect to SAP**.

   If the SAP username and password are entered correctly, a **Connection Successful** message appears.

1. (Optional) Under **Optional AppFlow Configuration**, **Step 1 - Download the JSON template file**, choose **Download the existing JSON template file** to modify the appflow ingestion settings.
**Note**
You can use your own editor to edit the .json file. You cannot edit the .json file in AWS Supply Chain.

   After you update the .json file, under **Step 2 - Upload the modified JSON template file**, choose **browse files** to upload.
**Note**
If this upload is unsuccessful, the **Upload summary** will display the errors or conflicts in the .json file. You can update the .json file to fix the issues and re-upload the file.

   Here is a sample .json file with the required schedule, data flows, and source tables.

   ```
   {
       "schedule" : {
           "scheduleExpression"  : "rate(1days)", // scheduleExpression key should be available and the value cannot be null/empty. Format starts with rate and having time values in minutes, hours, or days. For example, rate(1days)
           "scheduleStartTime" : null // Supported format - "yyyy-MM-dd'T'hh:mm:ss[+|-]hh:mm". For example, 2022-04-26T13:00:00-07:00. ScheduleStartTime should atleast be 5 minutes after current time. A null value will automatically set the start time as 5 minutes after the connection creation time
       },
       "dataFlows" : [ // DataFlows cannot be null or empty. Make sure to choose from the list below
           "Company-Company",
           "Geography-Geography",
           "Inventory-Inventory Level",
           "Inventory-Inventory Policy",
           "Outbound-Outbound Order Line",
           "Outbound-Outbound Shipment",
           "Product-Product",
           "Product-Product Hierarchy",
           "Production Order-Inbound Order",
           "Production Order-Inbound Order Line",
           "Purchase Order-Inbound Order",
           "Purchase Order-Inbound Order Line",
           "Purchase Order-Inbound Order Line Schedule",
           "Reference-Reference Fields",
           "Shipment-Shipment",
           "Site-Site",
           "Site-Transportation Lane",
           "Trading Partner-Trading Partner",
           "Transfer Order-Inbound Order Line",
           "Vendor Management-Vendor Lead Time",
           "Vendor Management-Vendor Product",
           "Product-Product UOM"
       ],
       "sourceTables" : [   // sourceTables cannot be empty
           {
               "tableName" : "SomeString", // Should be an existing table name from the SAP instance
               "extractType" : "DELTA",      // Should either be DELTA or FULL
               "tableCols" : [    // TableCols cannot be empty. Enter valid column names for the table
                   "col1",
                   "col2",
                   "col3"
               ],
               "filters" : [// Optional field
                       "colName" : "col1", // colName value should be part of tableCols
                       "dataType" : "String",  // Should contain values `STRING` or `DATETIME`
                       "value" : "String",
                       "operator" : "String"  // Choose a string value from the pre-defined value of "PROJECTION", "LESS_THAN", "CONTAINS","GREATER_THAN","LESS_THAN_OR_EQUAL_TO","GREATER_THAN_OR_EQUAL_TO","EQUAL_TO","NOT_EQUAL_TO","ADDITION","MULTIPLICATION","DIVISION","SUBTRACTION","MASK_ALL","MASK_FIRST_N","MASK_LAST_N","VALIDATE_NON_NULL","VALIDATE_NON_ZERO","VALIDATE_NON_NEGATIVE",or "VALIDATE_NUMERIC","NO_OP";
               ]
           },
           {

               // sourceTables with same keys - tableName, extractType, tableCols, filters(not mandatory)

           }
       ]
   }
   ```

1. Under **Amazon S3 Bucket Billing**, review the Amazon S3 billing information, and then select **Acknowledge**.

1. Choose **Next**.

1. Under **Data Mapping**, choose **Get started**.

1.
**Note**
The required fields are already mapped. Perform this step only if you want to make specific changes to the default transformation recipe.

   On the **Mapping Recipe** page, you can view the default transformation recipe under **Field mappings**.

   Choose **Add mapping**, to map any additional destination field. The **Required Destination Fields** are mandatory. Choose **Destination field** to add an additional custom destination field.

1. To view the source field values and data mappings from the transformation recipe, you can upload sample data. On the **Mapping Recipe** page, under **Upload sample data**, choose **browse files**, or drag and drop files. The sample data file must contain the required parameters and include the source field names.

1. Choose **Accept all and continue**.

1. Under **Review and confirm**, you can view the data connection summary. To edit your data field mapping, choose **Go back to Data Mapping**.

1.  (Optional) Under **Recipe Actions**, you can do the following:
   + **Download recipe file** - Select **Download** to edit your recipe files in SQL as a text file.
**Note**
For information about built-in SQL functions, see [Spark SQL](https://spark.apache.org/docs/latest/api/sql/index.html).
   + **Upload recipe file** - Choose **browse files** or drag and drop your edited recipe text files. Select **Confirm upload** to upload the edited recipe file and modify your data field mappings.

1. To review the Amazon S3 location paths where you must upload your SAP source data for ingestion, choose **Confirm and configure data ingestion**. Alternatively, you can choose **Confirm and configure data ingestion later**. You can view the data ingestion information anytime. From the AWS Supply Chain dashboard, select **Connections**. Select the connection dataflow that you want to ingest data, choose the vertical ellipsis, and select **Ingestion setup**.

## SAP data sources
<a name="s4-datasources"></a>

Configure the following SAP table sources for AWS Supply Chain to connect and extract information.

**Note**
When you search for an SAP data source, prefix the data source name with *EntityOf*. For example, for the data source *0BP\_DEF\_ADDRESS\_ATTR*, the entity name should be *EntityOf0BP\_DEF\_ADDRESS\_ATTR*.
When Amazon AppFlow extracts each SAP data source, the entity name format is used to extract information. For example, to extract data from *0BP\_DEF\_ADDRESS\_ATTR*, the data is extracted from the entity path */sap/opu/odata/sap/Z0BP\_DEF\_ADDRESS\_ATTR\_SRV/EntityOf0BP\_DEF\_ADDRESS\_ATT*.

| SAP data source | SAP data source description​ | SAP source table | OData service name | BW data source | SAP data | Delta​/Full |
| --- | --- | --- | --- | --- | --- | --- |
| 0BP\_DEF\_​ADDRESS\_ATTR | BP standard address ​extraction | NA | Z0BP\_DEF\_​ADDRESS\_ATTR​\_SRV | Data source | Master data | Delta |
| 0BPARTNER\_​ATTR | BP: BW Extraction ​Central Data | NA | Z0BPARTNER\_​ATTR\_SRV | Data source | Master data | Delta |
| 0BPARTNER\_​TEXT | BP: DataSource for ​Business Partner Texts | NA | Z0BPARTNER\_​TEXT\_SRV | Data source | Master data | Delta |
| 0CO\_PC\_ACT​\_05 | Material Valuation:​ Prices | NA | Z0CO\_PC\_​ACT\_05\_SRV | Data source | Master data | Full |
| 0COMP\_CODE​\_TEXT | Company Code ​Text | NA | Z0COMP\_CODE​\_TEXT\_SRV | Data source | Master data | Full |
| 0CUSTOMER\_​ATTR | Customer | NA | Z0CUSTOMER\_​ATTR\_SRV | Data source | Master data | Delta |
| 0MAT\_VEND\_​ATTR | Material or Vendor | NA | Z0MAT\_VEND\_​ATTR\_SRV | Data source | Master data | Delta |
| 0MATERIAL\_​ATTR | Material | NA | Z0MATERIAL\_​ATTR\_SRV | Data source | Master data | Delta |
| 0MATERIAL\_​TEXT | Material text | NA | Z0MATERIAL\_​TEXT\_SRV | Data source | Master data | Delta |
| 0PURCH\_ORG\_​TEXT | Purchasing ​org text | NA | Z0PURCH\_ORG\_​TEXT\_SRV | Data source | Master data | Full |
| 0VENDOR\_​ATTR | Vendor | NA | Z0VENDOR\_​ATTR\_SRV | Data source | Master data | Delta |
| 2LIS\_02\_HDR | Purchasing Data ​(Header Level) | NA | Z2LIS\_02\_​HDR\_SRV | Data source | Transa​ctional | Delta |
| 2LIS\_02\_ITM | Purchasing Data ​(Item Level) | NA | Z2LIS\_02\_​ITM\_SRV | Data source | Transa​ctional | Delta |
| 2LIS\_02\_SCL | Purchasing Data ​ (Schedule Line Level) | NA | Z2LIS\_02\_​SCL\_SRV | Data source | Transa​ctional | Delta |
| 2LIS\_02\_SCN | Confirmation of​ Schedule Lines | NA | Z2LIS\_02\_​SCN\_SRV | Data source | Transa​ctional | Delta |
| 2LIS\_03\_BF | Goods Movements from​ Inventory Management | NA | Z2LIS\_03\_​BF\_SRV | Data source | Transa​ctional | Delta |
| 2LIS\_04\_P​\_MATNR | Material View ​from PP/PP-PI | NA | Z2LIS\_04\_P\_​MATNR\_SRV | Data source | Transa​ctional | Delta |
| 2LIS\_08TRFKP | Shipment Costs​ at Item Level | NA | Z2LIS\_08TRFKP​\_SRV | Data source | Transa​ctional | Delta |
| 2LIS\_08TRTLP | Shipment: Delivery​ Item Data by Section | NA | Z2LIS\_08TRTLP​\_SRV | Data source | Transa​ctional | Delta |
| 2LIS\_08TRTK | Shipment: Header​ Data | NA | Z2LIS\_08TRTK​\_SRV | Data source | Transa​ctional | Delta |
| 2LIS\_11​\_VAHDR | Sales Document ​Header | NA | Z2LIS\_11​\_VAHDR\_SRV | Data source | Transa​ctional | Delta |
| 2LIS\_11​\_VAITM | Sales Document​ Item | NA | Z2LIS\_11\_​VAITM\_SRV | Data source | Transa​ctional | Delta |
| 2LIS\_12\_VCITM | Delivery Item​ Data | NA | Z2LIS\_12​\_VCITM\_SRV | Data source | Transa​ctional | Delta |
| ZADRC | Addresses | ADRC | ZADRC\_SRV | Table | Master data | Full |
| ZBUT021\_FS | Partner Address | BUT021\_FS | ZBUT021\_FS​\_SRV | Table | Master data | Full |
| ZCDHDR | Change document ​header | CDHDR | ZCDHDR\_SRV | Table | Master data | Delta |
| ZEINA | Purchasing Info ​Record: General ​Data | EINA | ZEINA\_SRV | Table | Master data | Full |
| ZEINE | Purchasing Info ​Record: Purchasing ​Organization Data | ZV\_EINE | ZEINE\_SRV | Table | Master data | Full |
| ZEKKO | Purchasing Document ​Header | ZV\_EKKO | ZEKKO\_SRV | Table | Transa​ctional | Delta |
| ZEKPO | Purchasing Document​ Item | ZV\_EKPO | ZEKPO\_SRV | Table | Transa​ctional | Delta |
| ZEQUI | Equipment master​ data | EQUI | ZEQUI\_SRV | Table | Master data | Full |
| ZGEOLOC | Geo Location | GEOLOC | ZGEOLOC\_SRV | Table | Master data | Full |
| ZLIKP | Delivery Header​ Data | LIKP | ZLIKP\_SRV | Table | Transa​ctional | Delta |
| ZLIPS | Delivery: Item​ Data | ZV\_LIPS | ZLIPS\_SRV | Table | Transa​ctional | Delta |
| ZMDRP\_​NODTT | Node Type for ​DRP Network | MDRP\_NODTT | ZMDRP\_NODTT​\_SRV | Table | Master data | Full |
| ZMARC | Plant Data for ​Material | ZQ\_MARC | ZMARC\_SRV | Table | Master data | Full |
| ZMARD | Storage Location ​Data for ​Material | ZQ\_MARD | ZMARD\_SRV | Table | Master data | Full |
| ZMCHB | Batch Stocks | ZQ\_MCHB | ZMCHB\_SRV | Table | Master data | Full |
| ZT001W | Plant | T001W | ZT001W\_SRV | Table | Master data | Full |
| ZT005T | Country Names | T005T | ZT005T\_SRV | Table | Master data | Full |
| ZT141T | Descriptions of ​Material Status | T141T | ZT141T\_SRV | Table | Master data | Full |
| ZT173T | Shipping Type of​ Transport Texts | T173T | ZT173T\_SRV | Table | Master data | Full |
| ZT179 | Materials: ​Product Hierarchies | T179 | ZT179\_SRV | Table | Master data | Full |
| ZT179T | Materials: ​Product Hierarchies Text | T179T | ZT179T\_SRV | Table | Master data | Full |
| ZT370U | Equipment Category Text | T370U | ZT370U\_SRV | Table | Master data | Full |
| ZT618T | Mode of Transport​ Descriptions | T618T | ZT618T\_SRV | Table | Master data | Full |
| ZTVRAB | Route Stages | TVRAB | ZTVRAB\_SRV | Table | Master data | Full |
| ZTVRO | Routes | TVRO | ZTVRO\_SRV | Table | Master data | Full |
| ZVALW | Route Schedule | VALW | ZVALW\_SRV | Table | Master data | Full |
| ZVBBE | Sales Requirements:​ Individual Records | VBBE | ZVBBE\_SRVs | Table | Master data | Full |
| ZINB\_​SHIPMENT | Shipment Header ​and Item (Inbound) | ZV\_INB\_​SHIPMENT​ based with join ​condition: VTTK.MANDT = VTTP.MANDT​ and ​VTTK.TKNUM = VTTP.TKNUM | ZINB\_SHIPMENT​\_SRV | Table | Transa​ctional | Full |
| ZAUFK | Order Master Data | AUFK | ZAUFK\_SRV | Table | Master data | Full |
| ZMARM | Unit of Measure for Material | MARM | ZMARM\_SRV | Table | Master data | Full |
| ZEBAN | Purchase requisitions | EBAN | ZEBAN\_SRV | Table | Transactional data | Delta |
