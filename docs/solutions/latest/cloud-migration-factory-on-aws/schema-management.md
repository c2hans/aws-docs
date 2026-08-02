---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/schema-management.html
---

# Schema management
<a name="schema-management"></a>

The Cloud Migration Factory on AWS solution provides a fully extensible metadata repository, allowing data for automation, auditing and status tracking to be stored in a single tool. The repository provides a default set of entities (Waves, Applications, Servers, and Databases) and attributes at deployment time to get you started with capturing and using the most frequently used data, and from here you can customize the schema as required.

Only Cognito admin group users have permissions to manage the schema. To make a user a member of the admin or other groups, refer to [User management](permission-management.md).

Go to **Administration**, and select **Attributes** for the default entity tabs. The following tabs are available to support management of the entity.

 **Attributes** - Allows for adding, editing and deleting attributes.

 **Info Panel** - Allows for editing of the Info panel help content, this is shown on the right of the entities' screen in the Migration Management section.

 **Schema Settings** - Currently this tab only provides the ability to change the friendly name of the entity, this is the name that is shown on the user interface. If not defined, then the user interface uses the programmatic name of the entity.

You can also create custom assets when you need to map your own business specific entities into CMF. You can add a new custom asset by pressing the **\+** tab at the end of the row of entity names.

## Adding a new custom asset
<a name="adding-a-new-custom-asset"></a>

**Note**
Custom assets are a feature of the Wave Planning Manager (WPM) module. In order to use them, WPM must be enabled when you deploy CMF.

You may wish to add a new custom asset (schema) to CMF in case you have business case specific entities you wish to import. You can add a new custom asset via the **\+** symbol located at the end of the entity tabs.

When you select the **\+** symbol a new panel will pop up requesting the minimum required information to create a new asset.

![create new schema](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/create-new-schema.png)

After creating the new asset, you can add additional asset-specific attributes. See the [Adding/editing an attribute](#addingediting-an-attribute) section for more information.

## Adding/editing an attribute
<a name="addingediting-an-attribute"></a>

Attributes can be amended dynamically through the **Attributes** administration section of the Cloud Migration Factory on AWS solution. When attributes are added, edited or deleted the updates will be applied in real-time for the administrator making the change. Any other user that is currently logged into the same instance will have their session updated automatically within a minute of the changes being saved by the administrator.

Some attributes are defined as system attributes, which means that the attribute is key to the core functionality of Cloud Migration Factory on AWS and so only some properties are available for administrators to amend. Any attribute that is a system attribute will be shown with a warning on the top of the **Amend attribute** screen.

For system defined attributes only the following can be edited:
+ Info Panel
+ Advanced Options
  + Attribute Grouping & Positioning
  + Input Validation

All other properties of the system defined attribute are read-only.

Adding an attribute:

 **Attribute management**

![attribute management](http://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/attribute-management.png)

You can add new attributes by choosing the **Add** button on the attributes tab of the entity you wish to add the attribute to. In the example above, choosing **Add** will add a new attribute to the database entity.

On the **Amend attribute** dialog, you must to provide the following required properties:

 **Programmatic name** - This is the key that will be used to store data for the attribute against items in the DynamoDB table. It is also referenced when using the Migration Factory APIs, and in automation scripts.

 **Display name** - This is the label that will be displayed on the web interface against the data entry field.

 **Type** - This drop-down selection defines the type of data that the user will be allowed to store against the attribute. The following options are available:

| Type | Usage |
| --- | --- |
| String | Users can enter any single line of text carriage returns are not permitted. |
| Multivalue String | Similar to a **String** the only difference being that the user can enter multiple values on separate lines within the field, these are then stored as an array/list. |
| Password | Provides the user with a way to securely enter data that should not be displayed on the screen by default. Data is not stored encrypted when using this attribute type, and is shown in clear text when viewed in API payloads, thus should not be used to store sensitive data. Any passwords or secrets should be stored in the Migration Factory Credential Manager (covered in this document) which utilizes AWS Secrets Manager to securely store and provide access to credentials.  |
| Date | Provides a field with a date picker for the user to select a date, or they can manually enter the date required. |
| Checkbox | Provides a standard checkbox, when checked the key value will store '`true' if not checked then it will be '`false' or the key will not exist in the record. |
| TextArea | Unlike the **String** type **TextAreas** provide the ability to store multi line text, it supports basic text characters only. |
| Tag | Allows users to store a list of key/value pairs. |
| List | Provides the user a list of predefined options to select from, these options are defined in the schema attribute definition in the Value List property of the attribute. |
| Relationship | This attribute type provides the ability to store relationships between any two entities or records. When defining a relationship attribute you select the entity that the relationship will be to, and then the key value used to relate the items and select the attribute from the related item that you wish to display to the user.<br />The user is presented with a drop-down list based on the entity and display values available for the relationship.<br />Under each relationship field the user has a quick link to show the summary of the related item. |
| JSON | Provides a JSON editor field where JSON data can be stored and edited. This could be used for storing script input/output parameters or other data needed for automation of tasks, or any other use. |

When adding a new attribute, you must grant users access to the new attribute through a policy. See the [Permission management](permission-management.md) section for details on how to grant attribute access.

### Info panel
<a name="info-panel"></a>

Provides the facility to specify contextual help and guidance for the attribute’s usage. When specified, the attribute’s label on the UI will have an **Info** link displayed to the right. Clicking this link provides the user with the **Help content** and **Help links** specified in this section to the right of the screen.

The Info panel section provides two views of the data, the **Edit** view where you can define the content, and the **Preview** view to provide a quick preview of what the user will see when updates to the attribute are saved.

The **Help title** supports only plain text values. The **Help content** supports a subset of html tags that allow text formatting. For example, adding <b> start and </b> end tags around the text will make the enclosed text bold (i.e. <b>Network Interface ID</b> would result in **Network Interface ID**). The supported tags are as follows:

| Tag | Usage | UI Example |
| --- | --- | --- |
| <p></p> | Defines a paragraph. | <p>My first paragraph</p><br /><p>My second paragraph</p> |
| <a> | Defines a hyperlink. | <a href="https://aws.amazon.com/">Visit AWS\!</a> |
| <h3>, <h4> and <h5> | Defines headings h3 to h5 | <h3>My heading 3</h3> |
| <span> | Defines a section of text, allowing additional formatting to be applied, such as text color, size, font. | <span style="color:blue">blue</span> |
| <div> | Defines a block of the document, allowing additional formatting to be applied, such as text color, size, font. | <div style="color:blue"><br /><h3>This is a blue heading </h3><br /><p>This is some blue text in a div.</p><br /></div> |
| <ul> \+ <li> | Defines an unordered bulleted list. | <ul><br /><li>Rehost</li><br /><li>Replatform</li><br /><li>Retire</li><br /></ul> |
| <ol>, <li> | Defines an ordered/numbered list. | <ol><br /><li>Rehost</li><br /><li>Replatform</li><br /><li>Retire</li><br /></ol> |
| <code> | Defines a block or section of text containing code. | <code>background-color</code> |
| <pre> | Defines a block of preformatted text, all line breaks, tabs, and spaces are output. | <pre><br />My preformatted text.<br />This is displayed in a fixed width font and will display as typed <<these spaces will be shown.<br /></pre> |
| <dl>, <dt> and <dd> | Defines a description list. | <dl><br /><dt>Rehost</dt><br /><dd>Lift and shift migration</dd><br /><dt>Retire</dt><br /><dd>Decommission the instance or service </dd><br /></dl> |
| <hr> | Defines a horizontal rule across the page to show a switch in topic or section. | <hr> |
| <br> | Defines a line break in text. These are supported but not required as any carriage returns in the editor will be replaced with <br> when saved. | <br> |
| <i> and <em> | Defined the enclosed text in *Italic* or alternative localized format. | <i>This is in Italic</i> or <em>This is also Italic</em> |
| <b> and <strong> | Defines the enclosed text in **bold** font. | <b>I’m in bold</b> or <strong>This is different</strong> |

Another option available to provide help is links to external content and guidance. To add an external link to the attribute’s contextual help click **Add new URL** and provide a **Label** and URL. You can add multiple links to the same attribute type as required.

### Advanced options
<a name="advanced-options"></a>

#### Attribute grouping and positioning
<a name="attribute-grouping-positioning"></a>

This section provides the administrator with the ability to set where on the Add/Edit UI the attribute will be positioned and also allows for grouping of attributes providing the user with a simple way to locate related attributes.

 **UI Group** is a text value that defines the name of the group that the attribute should be shown in, all attributes with the same UI Group value will be placed in the same group, any attribute with no UI Group specified will be placed in the default group at the top of the form entitled **Details**. When UI Group is specified the user interface will display the text shown here as the title of the group.

The second property in this section is **Order in group**, this can be set to any positive or negative number, and when specified the attributes will be listed based on a sort of lowest to highest based on this value. Any attributes that do not have an **Order in group** specified will be lower priority and sorted alphabetically.

#### Input validation
<a name="input-validation"></a>

This section allows the administrator to define validation criteria that ensures that the user has entered valid data before they are able to save an item. The validation uses a regular expression or regex string which is a series of characters that specify a search pattern for a text value. For example, the pattern **^(subnet-([a-z0-9]{17})**)$\* will search for the text **subnet-** followed by any combination of the characters a to z (lowercase) and digits 0 to 9 with an exact number of characters of **17**, if it finds anything else it will return false indicating that the validation has failed. Within this guide we cannot cover all the possible combinations and patterns available, but there are many resources on the internet that can provide help on creating the prefect on for your use case. Here are some common examples to get you started:

| Regex Pattern | Usage |
| --- | --- |
| ^(?\!\\s\*$).\+ | Ensures that the value is set. |
| ^(subnet-([a-z0-9]{17})\*)$ | Checks that the value is a valid subnet ID.<br />[Starts with the text **subnet-** followed by 17 characters made up of letters and numbers only] |
| ^(ami-(([a-z0-9]{8,17})\+)$) | Check that the value is a valid AMI ID.<br />[Starts with the text **ami-** followed by between 8 and 17 characters made up of letters and numbers only] |
| ^(sg-([a-z0-9]{17})\*)$ | Checks that the value is in a valid security group ID format.<br />[Starts with the text **sg-** followed by 17 characters made up of letters and numbers only] |
| ^(([a-zA-Z0-9]\|[a-zA-Z0-9]** [a-zA-Z0-9])\\.) **([A-Za-z0-9]\|[A-Za-z0-9][A-Za-z0-9\\-]\*[A-Za-z0-9])$ | Ensures that server names are valid and only contain alphanumeric characters, hyphens and periods. |
| ^([1-9]\|[1-9][0-9]\|[1-9][0-9][0-9]\|[1-9][0-9][0-9][0-9]\|[1][0-6][0-3][0-8][0-4])$ | Ensures that a number is entered that is between 1 and 1634. |
| ^(standard\|io1\|io2\|gp2\|gp3)$ | Ensures that the string enter matches either standard, io1, io2, gp2 or gp3. |

Once you have created your regex search pattern, you can specify the specific error message that will be shown to the user under the field, enter this into the **Validation help message** property.

Once these two properties are set then in the same screen you will see below a **Validation simulator**, here you can test that your search pattern is working as expected and that the error message is displayed correctly. Just type some test text into the **Test validation** field to verify the pattern is matched correctly.

#### Example data
<a name="example-data"></a>

The example data section provides the administrator with the ability to show the user an example of data format required for an attribute, this can be specified for the format of data required when provided in an intake form upload, through the user interface and/or through the API directly.

Example data shown in the **Intake form example data** property will be output in any intake template created where the attribute is included, when using the **Download, a template intake form** function, under **Migration Management > Import**.

User interface example data and API example data are stored in the attribute, but not currently exposed in the web interface. These can be used in integrations and scripts.
