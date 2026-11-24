---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/asset-templates.html
---

# Asset templates

An asset template defines the rules for a kind of asset. It sets how assets are named and where their content can be uploaded, imported, or derived from and published to. It also sets which attributes they carry, which file types and folders they can hold, what their state lifecycle is, and which other connectors can act on them. Every project that uses a template applies the same rules to its assets, so assets of one kind stay consistent. For the full list, see [What a Template Controls](#template-settings).

## Why Use Asset Templates
<a name="template-why"></a>

Content is only useful if the next person, or the next job, can rely on it. Without agreed rules, one team names a capture by date and another by site. One upload carries a sensor and another does not. Training jobs, scripts, and reviewers each have to cope with every variation.

A template is the contract for a kind of asset. SDMA checks every asset against its template when the asset is created and each time it is updated, so whatever reads the asset can rely on its shape. The template also names the connectors that can act on the asset, so one place defines both what the data looks like and what is allowed to happen to it.

| You want to | Set in the template |
| --- | --- |
| Make every upload say where, when, and with what it was captured | Required asset attributes and file attributes. See [Attributes](#template-attributes). |
| Keep names searchable and consistent | An asset name rule. See [Asset Names](#template-names). |
| Let people choose from values that another system owns, such as a list of sites | An attribute whose choices come from a connector. See [Values from Connectors](#template-connector-values). |
| Accept only the file types a workflow can use, and refuse the rest | Allowed and disallowed file types. See [File Types and Content Analysis](#template-file-types). |
| Make every dataset put its inputs in the same place, so jobs find them without configuration | Folder structure. See [Folder Structure](#template-folders). |
| Hold new content until someone has looked at it | Review states. See [Asset Review States](#template-states). |
| Have previews, conversions, or model runs happen on every upload without anyone asking | Connectors. See [Connectors](connectors.md). |
| See at a glance how content moves through those connectors | The **Content flow** tab. See [See How Content Flows Through the Connectors](#template-content-flow). |

## What a Template Controls
<a name="template-settings"></a>

| Setting | What it does |
| --- | --- |
| Name and description | Identify the template. The description is optional, up to 1,024 characters, and appears in template lists and pickers. |
| Asset name rule | A regular expression that an asset’s whole name must match. |
| Review states | Whether new and updated assets start as drafts that someone reviews, or are ready at once. |
| Asset attributes | The attributes an asset carries, and which are required. |
| File attributes | The attributes each file carries, and which are required. |
| File types | Which file types are not allowed, which are expected, and what SDMA does with each after upload. |
| Folder structure | The folders and files that an asset must or may contain. |
| Content analysis | Whether SDMA inspects files, generates previews, and suggests attributes. |
| Connectors | Which connectors can act on assets that use the template. See [Connectors](connectors.md). |

## Create or Edit a Template
<a name="template-create"></a>

In the Spatial Data Portal, open **Library settings**, open the **Content** tab, and use the asset templates table. You can create a template, or copy an existing one and change the copy. You need Contributor access or higher on the library to create a template.

The template editor has these tabs:
+  **Template** – The settings in the preceding table.
+  **Content flow** – A visual representation of how content is acted upon by the template’s connectors. It appears when the template has connectors. See [See How Content Flows Through the Connectors](#template-content-flow).
+  **JSON configuration** – The same settings as a JSON document, for copying a template between libraries or for settings that the form does not show. Fix any JSON errors before you return to the **Template** tab.
+  **Access management** – Who can view and change the template. See [Access Management](access-control.md).
+  **Associated projects** – The projects that use the template, and their requests to use it.

Each time you save a template, SDMA creates a new version of it. SDMA refuses to save a template whose configuration breaks its own rules, such as an unknown state progression or attributes whose dependencies form a loop. When you save a template that assets already use, the Portal shows a note with the new version.

## Asset Names
<a name="template-names"></a>

 **Asset name regular expression** is matched against the whole name. For example, `^[A-Za-z0-9_-]+$` allows only letters, digits, underscores, and hyphens. SDMA checks the name when an asset is created or renamed. If you tighten the rule later, assets that already exist keep their names.

## Asset Review States
<a name="template-states"></a>
+  **Draft until reviewed** – This is the default. New and updated assets are drafts. They have limited visibility until someone marks them reviewed.
+  **Ready immediately** – New and updated assets are ready for use, and visible to all applicable users.

In the template JSON, `stateProgression` is `["draft", "reviewed"]` or `["ready"]`.

## Attributes
<a name="template-attributes"></a>

A template has two attribute lists. **Asset attributes** describe the asset as a whole. **File attributes** apply to every file in the asset. A file type can also have its own attributes (see [File Types and Content Analysis](#template-file-types)).

For each attribute, you choose:
+  **Name** – Unique within its list.
+  **Data type** – `string`, `number`, `boolean`, or `date`.
+  **Multiple values** – Turn this on to let the attribute hold a list of values. In the JSON it is a `list` with an `itemType`.
+  **Required** – A required attribute must have a value. An optional attribute can be left empty.
+  **Constraints** – Rules for the value (see the following table).
+  **Source** – `user` for a value that people enter, or a connector that fills the value in.

| Data type | Constraints |
| --- | --- |
|  `string`  |  `const` (a fixed value), `enum` (a list of allowed values), `default`  |
|  `number`  |  `const`, `enum`, `min`, `max`, `default`  |
|  `boolean`  |  `default`  |
|  `date`  |  `const`, `format`, `min`, `max`  |
| list |  `allowedValues`, `itemType`, `minItems`, `maxItems`  |

Constraints go in the attribute’s `value` object. An attribute with a constraint of `const` is read-only.

### Attributes That the Template Does Not List
<a name="template-additional-attributes"></a>

Set `allowAdditionalAttributes` to `false` to close a list. The Portal then lets people enter only the attributes that the list names. SDMA also refuses a connector write that names an attribute outside the list. The connector run fails, names the attributes, and writes nothing. Auto-accepted attribute suggestions with undeclared names stay as suggestions. New templates that you create in the Portal start with additional asset attributes turned off.

### Values from Connectors
<a name="template-connector-values"></a>

An attribute can get its values from a connector in two ways:
+  **Fill the value.** The connector writes the value when a configured lifecycle event happens. Set the attribute’s source to the connector.
+  **Offer a list of values.** The connector supplies the choices for people to pick from. Set the attribute’s `constraintSource` to the connector.

A field can depend on another field, so that the field is enabled only after its parents have values. The Portal filters the choices by the parents' values. A field can depend only on attributes in the same list, and the dependencies cannot form a loop. When a field depends on an attribute that comes from another connector, the field’s own connector must accept that attribute as an input. For more information, see [Connector Configuration](connector-configuration.md).

## File Types and Content Analysis
<a name="template-file-types"></a>

 **Content analysis and transformation** sets what SDMA does after upload:
+  **Verify files** – SDMA inspects uploaded files. Previews and attribute suggestions need it.
+  **Generate previews** – SDMA creates previews for files of known types.
+  **Suggest attributes** – SDMA extracts attributes and suggests them. Auto-extraction is supported for E57, LAZ, GLB, glTF, and image files.

Under **Attribute suggestions**, choose what happens to the suggested attributes:
+  **Automatically accept pre-selected suggestions** – SDMA accepts the attributes that you list for each file type.
+  **Automatically accept all suggestions** – SDMA accepts every suggestion.
+  **Review all suggestions manually** – A person accepts or dismisses each one.

To configure individual file types, choose **Yes** for **Provide configuration by file type**. For each file extension you can set what SDMA does with files of that type, add attributes that apply to that type only, and list the suggested attributes that SDMA accepts automatically.

You can also list file types that are **not allowed**. SDMA refuses an asset that contains a file of a disallowed type, when the asset is created or updated. Write the extension with or without the leading dot, for example `exe`.

When **Allow additional file types not listed below** is off, and the template lists at least one file type, SDMA refuses a file of any other type. The Portal flags it as you work. If the list is empty, any type is allowed unless it is in the not-allowed list.

## Folder Structure
<a name="template-folders"></a>

By default an asset can hold any folders. To restrict them, choose **Restrict to specific folder structure** and add paths.
+ A path that ends in `/`, such as `raw/`, is a folder. It covers the folder and its subfolders.
+ Any other path is a file, such as `calibration.json`, or a file pattern. In a pattern, ` ` matches within one folder, and ` ` matches across folders. For example, `data/` matches TIFF files directly in `data/`, and `data/` matches them at any depth. A path with no `` and no trailing `/` matches that file, and also everything under a folder of that name, so `data` covers `data/a.tif`.
+ Mark a path **required** to make SDMA require a file in that folder, or the file itself, when the asset is created.
+ Optionally list the **file types** that a folder accepts.

Every file must match a path in the list. SDMA checks the paths in order and uses the first one that matches. If that path lists file types, the file’s type must be one of them. SDMA ignores its own system files.

## See How Content Flows Through the Connectors
<a name="template-content-flow"></a>

When connectors are attached to a template, the template editor has a **Content flow** tab. It shows what each connector does and how the connectors depend on each other, so you can check a design before assets use it.
+  **Each connector is a card.** The card shows the service that the connector calls, the files that start it, and the files that it produces.
+  **Arrows join connectors through files.** When one connector writes a file that another connector’s trigger matches, an arrow joins them. Connectors work together through the asset record, so the arrows show the chain that runs after an upload. See [Chaining Connectors](connector-configuration.md#chaining-connectors).
+  **Cards show what a connector records.** **Provenance attributes** are values that say what produced a result, such as the model and the source coordinate system. **Findings** are values that describe what the connector found. A connector marks each mapping as provenance or finding by using the `role` field. See [Saying What a Value Means](connector-configuration.md#field-mapping-role).
+  **Cards show the model.** When a trigger declares which model it runs, the card names it. See [Naming the Model a Trigger Runs](connector-configuration.md#trigger-model-identity). The **AI pipeline** summary at the top counts the governed models and connectors in the chain, and the file the chain produces.
+  **Dashed arrows mark a guess.** A dashed arrow means that more than one connector writes a file that the next connector matches. To make the link explicit, name the file with `fileNameRegex` in the producer’s output filter.
+  **A warning marks a broken chain.** **Check this flow** lists a trigger that starts on a derived file that no other connector in the template writes.

The tab shows connectors that you have added but not saved with a **Not saved yet** label. Fix any JSON errors before you open it.

## How Templates Are Applied
<a name="template-apply"></a>
+  **Projects use templates.** A project can create assets from a template only after the project and the template are associated. The project requests the association, and an Owner or Manager of the template approves it. See [Access Management](access-control.md). If the project does not allow assets without a template, every asset in it needs one.
+  **An asset keeps its template.** You pick the template when you create the asset. You cannot change an asset’s template afterward.
+  **Checks run on create and update.** SDMA checks the asset’s name, attributes, file types, and folders when it is created. It checks them again whenever the asset is updated, against the template’s latest version. It records the version it used. An upload that breaks the rules is rejected.
+  **Editing a template does not change existing assets.** An existing asset is checked against the new version the next time it is updated. In the Portal, the template’s **Associated projects** tab shows whether each asset conforms to the current version.
+  **The template approves connectors.** A connector acts on an asset only if the connector is a default connector or the template lists it. See [Connectors](connectors.md).

## Example
<a name="template-example"></a>

The following template describes survey deliveries. Asset names use letters, digits, underscores, and hyphens. Every asset needs a `siteCode`, and can have a `region` and `tags`. Every file can have a `resolutionCm`. Executable files are not allowed, and files go in `raw/` or `processed/`.

```json
{
  "description": "Survey deliveries from field teams",
  "assetNameRegex": "^[A-Za-z0-9_-]+$",
  "stateProgression": ["draft", "reviewed"],
  "fileVerification": true,
  "previewGeneration": true,
  "attributeSuggestion": true,
  "assetMetadataConfig": {
    "optionalAttributes": [
      {
        "name": "region",
        "type": "string",
        "source": "user",
        "value": { "enum": ["emea", "amer", "apac"] }
      },
      {
        "name": "tags",
        "type": "list",
        "source": "user",
        "value": { "itemType": "string", "maxItems": 10 }
      }
    ],
    "allOf": [
      {
        "contains": {
          "properties": {
            "name": { "const": "siteCode" },
            "type": { "const": "string" },
            "source": { "const": "user" }
          },
          "required": ["name", "type", "value"]
        }
      }
    ],
    "allowAdditionalAttributes": false
  },
  "fileMetadataConfig": {
    "optionalAttributes": [
      {
        "name": "resolutionCm",
        "type": "number",
        "source": "user",
        "value": { "min": 1, "max": 500 }
      }
    ]
  },
  "fileTypes": {
    "files": {
      "laz": { "previewGeneration": true, "attributeExtraction": true },
      "e57": { "previewGeneration": true }
    },
    "allowAdditionalFileTypes": true,
    "disallowed": ["exe"]
  },
  "permittedFolderStructure": [
    { "path": "raw/", "required": true, "allowedFileTypes": ["laz", "e57"] },
    { "path": "processed/" }
  ]
}
```

In this JSON, a required attribute appears in `allOf`, and an optional one in `optionalAttributes`. The Portal builds this structure for you when you turn on **Required**.
