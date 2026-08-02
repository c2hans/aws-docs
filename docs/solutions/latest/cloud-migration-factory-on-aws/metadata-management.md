---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/metadata-management.html
---

# Metadata management
<a name="metadata-management"></a>

The Cloud Migration Factory on AWS solution provides an extensible datastore that allows records to be added, edited, and deleted from within the user interface. All updates to the data stored in the datastore are audited with record level audit stamps, which provide creation and update timestamps along with user details. All update access to records is controlled by the groups and associated policies that the logged in user is assigned. For more details about granting user permissions, refer to ** [Permission management](permission-management.md).**

## Viewing data
<a name="viewing-data"></a>

Through the **Migration Management** navigation pane, you can select the record types (application, wave, database, server) held in the datastore. After you select a view, a table of the existing records for the chosen record type is shown. Each record type’s table shows a default set of columns which can be changed by the user. Changes are persistent between sessions and are stored in the browser and computer used for making the changes.

### Custom assets
<a name="custom-assets-side-panel"></a>

**Note**
Custom assets are a feature of the Wave Planning Manager (WPM) module. In order to use them, WPM must be enabled when you deploy CMF.

If you have created any custom assets, they are listed under the **Custom Assets** navigation pane. Each asset will have its own sub-heading, and if you select one a table of the existing records for the chosen custom asset is shown. You can then proceed to create/edit/delete these records in the same manner as normal assets.

### Changing the default columns displayed in tables
<a name="changing-the-default-columns-displayed-in-tables"></a>

To change the default columns, select the settings icon located on the upper-right corner of any data table, and then select the columns to display. From this screen, you can also change the default number of rows to be displayed and activate line wrapping for columns with large amounts of data.

### Viewing a record
<a name="viewing-a-record"></a>

To view a specific record in a table, you can click anywhere on the row, or select the check box next to the row. Selecting multiple rows will result in no record being displayed. This will then display the record in read-only mode under the data table at the bottom of the screen. The displayed record will have the following default tables available.

 **Details** - This is a summary view of the required attributes and values for the record type.

 **All Attributes** - This displays a complete list of all the attributes and their values.

Other tabs may be present depending on the record type selected that provide related data and information. For example, **Application** records will have a **Servers** tab showing a table of the servers related to the **Application** selected.

## Adding or editing a record
<a name="adding-or-editing-a-record"></a>

Operations are controlled by record type through user permissions. If a user does not have the required permission to add or edit a specific type of record then the **Add** and/or **Edit** buttons are greyed out and deactivated.

To add a new record:

1. Choose **Add** from the upper-right corner of the table for the record type you want to create.

By default, the **Add application** screen displays the **Details** and **Audit** sections, but depending on the type and any customizations to the schema, other sections might display too.

1. Once you have completed the form and resolved all errors, choose **Save**.

To edit an existing record:

1. Select a record from the table you want to edit, then choose **Edit**.

1. Edit the record and ensure no validation errors exist, then choose **Save**.

## Deleting a record
<a name="deleting-a-record"></a>

If a user does not have the permission to delete a specific type of record then the **Delete** button is grayed out and deactivated.

**Important**
Records deleted from the datastore are not recoverable. We recommend making regular backups of the DynamoDB table, or exporting the data to ensure there is a recovery point in the event of an issue.

To delete one or more records:

1. Select one or more records from the table.

1. Choose **Delete** and confirm the action.

## Exporting data
<a name="exporting-data"></a>

The majority of data stored within the Cloud Migration Factory on AWS solution can be exported into Excel (.xlsx) files. You can export data at the record type level or a complete output of all data and types.

To export a specific record type:

1. Go to the table to export.

1.  *Optional*: Select the record(s) to export to an excel sheet. If none are selected, then all records will be exported.

1. Choose the **Export** icon in the upper-right corner of the data table screen.

An excel file with the name of the record type (for example, `servers.xlsx`) will be downloaded to the browser’s default download location.

To export all data:

1. Go to **Migration Management**, and select **Export.**

1. Check **Download All Data**.

An excel file with the name `all-data.xlsx` will be downloaded to the browser’s default download location. This excel file contains a tab per record type, and all records for each type will be exported.

**Note**
Exported files might contain new columns due to Excel having a cell text limit of 32767 characters. Hence, the export truncates the text for any fields that have more data than supported by Excel. For any truncated fields, a new column with the original name appended with the text `[truncated - Excel max chars 32767]` gets added to the export. Also, within the truncated cell, you will also see the text `[n characters truncated, first x provided]`. The truncation process protects against the scenario where a user exports and then imports the same Excel, and as a result, overwriting data with the truncated values.

## Importing data
<a name="importing-data"></a>

The Cloud Migration Factory on AWS solution provides a data import capability that can import simple record structures into the data store, for instance a list of servers. It can also import more complex relational data, for instance it could create a new application record and multiple servers contained in the same file and relate them to one another in a single import task. This allows a single import process to be used for any data type needed to be imported. The import process validates the data using the same validation rules used when the user edits data in the user interface.

### Downloading a template
<a name="downloading-a-template"></a>

To download template intake forms from the import screen, select the required template from the **Actions list**. The following two default templates are available.

 **Template with only required attributes** - This contains only the attributes marked as required. It provides the minimum set of attributes required to import data for all record types.

 **Template with all attributes** - This contains all the attributes in the schema. This template contains additional schema helper information for each attribute to identify the schema that it was found in. These helper prefixes to the column headers can be removed if required. If left in place during an import, the values within the column will only be loaded into the specific record type and not used for relational values. Refer to **Import header schema helpers** for more details.

### Importing a file
<a name="importing-a-file"></a>

Import files can be created in either .xlsx or .csv format. For CSV, it must be saved using UTF8 encoding, otherwise the file will appear to be empty when viewing the pre-upload validation table.

To import a file:

1. Go to **Migration Management**, and select **Import**.

1. Choose **Select file**. By default, you can only select files with either the `0csv` or `1xlsx` extensions. If the file is successfully read, then the file name and size of the file will be displayed.

1. Choose **Next**.

1. The **Pre-upload validation** screen shows the outcome of the mapping of the headers within the file to attributes within the schema, and validation of the values provided.
   + The mappings of the file column headers are shown on the on-screen table column names. To check which file column header was mapped, select the expandable name in the header for more information about the mapping, including the original file header and the schema name it has been mapped to. You will see a warning in the **Validation** column for any unmapped file headers, or where there are duplicate names in multiple schemas.
   + All headers validate the values for each row of the file against the requirements for the mapped attribute. Any warnings or errors in the file content are displayed in the **Validation column.**

1. Once no validation errors are present, choose **Next**.

1. The **Upload data** step shows an overview of the changes that will be made once this file is uploaded. For any item where a change will be performed on upload, you can select **Details** under the specific update type to view the changes that will be performed.

1. Once the review has been completed, choose **Upload** to commit these changes to the live data.

A message appears at the top of the form if the upload is successful. Any errors that occur during the upload are displayed under **Upload Overview**.

#### Import header schema helpers
<a name="import-header-schema-helpers"></a>

By default, the column headers in the intake file should be set to the name of an attribute from any schema, the import process searches all schemas and attempts to match the header name with an attribute. If an attribute is found in multiple schemas you will see a warning, especially for relationship attributes which can be ignored in most cases. However, if the intention is to map a specific column to a specific schema attribute then you can override this behavior by prefixing the column header with a schema helper prefix. This prefix is in the format `{attribute name}`, where `{schema name}` is the name of the schema based on its system name (wave, application, server, database) and the `{attribute name}` is the system name of the attribute in the schema. If this prefix is present then all values will only be populated into records for this specific schema, even if the attribute name is present in other schemas.

As shown in the following figure, the header in column C has been prefixed with `[database]`, forcing the attribute to map to the `database_type` attribute in the database schema.

 **Import header schema helper**

![import header schema helper](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/import-header-schema-helper.png)

#### Attribute import format
<a name="attribute-import-format"></a>

The following table provides a guide to formatting the values in an import file to import correctly into the Cloud Migration Factory attributes.

| Type | Supported import format | Example |
| --- | --- | --- |
| String | Accepts alphanumeric and special characters. |  `123456AbCd.!`  |
| Multivalue String | A list of string type, delimited by a semicolon. |  `Item1;Item2;Item3`  |
| Password | Accepts alphanumeric and special characters. |  `123456AbCd.!`  |
| Date | MM/DD/YYYY HH:mm |  `01/30/2023 10:00`  |
| Checkbox | Boolean value, in the form of a string, `TRUE` for selected, and `FALSE` for not selected. |  `TRUE` or `FALSE`  |
| Textarea | String type with support for line feeds and carriage returns. |  `Test line1` or `Testline 2`  |
| Tag | Tags must be formatted as `key=value;` multiple tags must be delimited by a semicolon. |  `TagKey1=Tagvalue1;TagKey2=tagvalue2;`  |
| List | If setting a single value list attribute use the same formatting as String type, if multiple selection list then, as per Multivalue String type. |  `Selection1;Selection2;`  |
| Relationship | Accepts alphanumeric and special characters that need to match with a value based on the key defined in the attribute definition. |  `Application1`  |
