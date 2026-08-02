---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/pkcs11-certificate-storage-api.html
---

# Certificate storage API operations
<a name="pkcs11-certificate-storage-api"></a>

 The following PKCS \#11 operations support the certificate object type (`CKO_CERTIFICATE`):

## General certificate operations
<a name="general-certificate-operations"></a>

**`C_CreateObject`**
Creates a new certificate object.

**`C_DestroyObject`**
Deletes an existing certificate object.

**`C_GetAttributeValue`**
Gets the value of one or more attributes of a certificate object.

**`C_SetAttributeValue`**
Updates the value of one or more attributes of a certificate object.

## Certificate object search operations
<a name="certificate-object-search-operations"></a>

**`C_FindObjectsInit`**
Starts a search for certificate objects.

**`C_FindObjects`**
Continues a search for certificate objects.

**`C_FindObjectsFinal`**
Ends a search for certificate objects.
