---
source_url: https://docs.aws.amazon.com/dcv/latest/websdkguide/getting-started.html
---

# Getting started with the Amazon DCV Web Client SDK
<a name="getting-started"></a>

 The Amazon DCV Web Client SDK comprises of a main `dcv.js` file and some auxiliary components. All the files are distributed inside a compressed archive that can be downloaded from the [Amazon DCV website](https://download.nice-dcv.com/webclientsdk.html) .

**To get started with the Amazon DCV Web Client SDK**

1. The Amazon DCV Web Client SDK archive is digitally signed with a secure GPG signature. To verify the archive's signature, you must import the NICE GPG key. To do so, open a terminal window and import the NICE GPG key.

   ```
   $ wget https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

   ```
   $ gpg --import NICE-GPG-KEY
   ```

1.  Download the **Amazon DCV Web Client SDK archive** and the **Amazon DCV Web Client SDK archive signature** from the [Amazon DCV website](https://download.nice-dcv.com/webclientsdk.html) .

1. Verify the signature of the Amazon DCV Web Client SDK archive using the signature.

   ```
   				$ gpg --verify
   				{{signature_filename.zip.sign}}
   				{{archive_filename.zip}}
   ```

   For example:

   ```
   $ gpg --verify nice-dcv-web-client-sdk-1.10.1-1011.zip.sign nice-dcv-web-client-sdk-1.10.1-1011.zip
   ```

1. If the signature verifies successfully, extract the contents of the Amazon DCV Web Client SDK archive and place the extracted directory on your web server. For example:

   ```
   				$ unzip
   				{{archive_filename.zip}}
   				-d /
   				{{path_to}}
   				/
   				{{server_directory}}
   				/
   ```
**Important**
You must retain the folder structure when deploying the Amazon DCV Web Client SDK on your web server.
When using Amazon DCV Web UI SDK, please beware that the `DCVViewer` React component expects the EULA.txt and third-party-licenses.txt files from this package to be present in the URL path for the embedded web server. The third-party-licenses.txt file should be modified to also include the content of the corresponding file from Amazon DCV Web Client SDK package and possibly any other license information from the libraries used by the consuming user application.
