---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/validate-generated-xml.html
---

# Validating Your Generated XML
<a name="validate-generated-xml"></a>

If you have written a script to automatically generate your profiles in xml, validate your output as follows.

**To validate your generated XML**

1. Generate a profile from your code and save it in your current directory.

1. Copy this `.xsd` file into your current directory: `/opt/elemental_se/web/public/schema/Live247Profile.xsd`.

1. Run the following command against your generated profile:

   ```
   xmllint --sax -noout -valid --schema Live247Profile.xsd <your xml filename>
   ```

   The system returns a response indicating whether the profile does or does not validate.
