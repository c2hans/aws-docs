---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-extract-content-from-pdf-files-using-amazon-textract.html
---

# Automatically extract content from PDF files using Amazon Textract
<a name="automatically-extract-content-from-pdf-files-using-amazon-textract"></a>

*Tianxia Jia, Amazon Web Services*

## Summary
<a name="automatically-extract-content-from-pdf-files-using-amazon-textract-summary"></a>

Many organizations need to extract information from PDF files that are uploaded to their business applications. For example, an organization could need to accurately extract information from tax or medical PDF files for tax analysis or medical claim processing.

On the Amazon Web Services (AWS) Cloud, Amazon Textract automatically extracts information (for example, printed text, forms, and tables) from PDF files and produces a JSON-formatted file that contains information from the original PDF file. You can use Amazon Textract in the AWS Management Console or by implementing API calls. We recommend that you use [programmatic API calls](https://aws.amazon.com/textract/faqs/) to scale and automatically process large numbers of PDF files.

When Amazon Textract processes a file, it creates the following list of `Block` objects: pages, lines and words of text, forms (key-value pairs), tables and cells, and selection elements. Other object information is also included, for example, [bounding boxes](https://docs.aws.amazon.com/textract/latest/dg/API_BoundingBox.html), confidence intervals, IDs, and relationships. Amazon Textract extracts the content information as strings. Correctly identified and transformed data values are required because they can be more easily used by your downstream applications.

This pattern describes a step-by-step workflow for using Amazon Textract to automatically extract content from PDF files and process it into a clean output. The pattern uses a template matching technique to correctly identify the required field, key name, and tables, and then applies post-processing corrections to each data type. You can use this pattern to process different types of PDF files and you can then scale and automate this workflow to process PDF files that have an identical format.

## Prerequisites and limitations
<a name="automatically-extract-content-from-pdf-files-using-amazon-textract-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ An existing Amazon Simple Storage Service (Amazon S3) bucket to store the PDF files after they are converted to JPEG format for processing by Amazon Textract. For more information about S3 buckets, see [Buckets overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) in the Amazon S3 documentation.
+ The `Textract_PostProcessing.ipynb` Jupyter notebook (attached), installed and configured. For more information about Jupyter notebooks, see [Create a Jupyter notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-prepare.html) in the Amazon SageMaker documentation.
+ Existing PDF files that have an identical format.
+ An understanding of Python.

**Limitations **
+ Your PDF files must be of good quality and clearly readable. Native PDF files are recommended, but you can use scanned documents that are converted to a PDF format if all the individual words are clear. For more information about this, see [PDF document preprocessing with Amazon Textract: Visuals detection and removal](https://aws.amazon.com/blogs/machine-learning/process-text-and-images-in-pdf-documents-with-amazon-textract/) on the AWS Machine Learning Blog.
+ For multipage files, you can use an asynchronous operation or split the PDF files into a single page and use a synchronous operation. For more information about these two options, see [Detecting and analyzing text in multipage documents](https://docs.aws.amazon.com/textract/latest/dg/async.html) and [Detecting and analyzing text in single-page documents](https://docs.aws.amazon.com/textract/latest/dg/sync.html) in the Amazon Textract documentation.

## Architecture
<a name="automatically-extract-content-from-pdf-files-using-amazon-textract-architecture"></a>

This pattern’s workflow first runs Amazon Textract on a sample PDF file (*First-time run*) and then runs it on PDF files that have an identical format to the first PDF (*Repeat run*). The following diagram shows the combined *First-time run* and *Repeat run *workflow that automatically and repeatedly extracts content from PDF files with identical formats.

![Using Amazon Textract to extract content from PDF files](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2d724523-2cab-42c9-a773-65857014d9ec/images/9e20070f-3e0c-46aa-aa98-a8b1eb3395dc.png)

The diagram shows the following workflow for this pattern:

1. Convert a PDF file into JPEG format and store it in an S3 bucket.

1. Call the Amazon Textract API and parse the Amazon Textract response JSON file.

1. Edit the JSON file by adding the correct `KeyName:DataType` pair for each required field. Create a `TemplateJSON` file for the *Repeat run* stage.

1. Define the post-processing correction functions for each data type (for example, float, integer, and date).

1. Prepare the PDF files that have an identical format to your first PDF file.

1. Call the Amazon Textract API and parse the Amazon Textract response JSON.

1. Match the parsed JSON file with the `TemplateJSON` file.

1. Implement post-processing corrections.

The final JSON output file has the correct `KeyName` and `Value` for each required field.

**Target technology stack  **
+ Amazon SageMaker
+ Amazon S3
+ Amazon Textract

**Automation and scale**

You can automate the *Repeat run* workflow by using an AWS Lambda function that initiates Amazon Textract when a new PDF file is added to Amazon S3. Amazon Textract then runs the processing scripts and the final output can be saved to a storage location. For more information about this, see [Using an Amazon S3 trigger to invoke a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html) in the Lambda documentation.

## Tools
<a name="automatically-extract-content-from-pdf-files-using-amazon-textract-tools"></a>
+ [Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) is a fully managed ML service that helps you to quickly and easily build and train ML models, and then directly deploy them into a production-ready hosted environment.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Textract](https://docs.aws.amazon.com/textract/latest/dg/what-is.html) makes it easy to add document text detection and analysis to your applications.

## Epics
<a name="automatically-extract-content-from-pdf-files-using-amazon-textract-epics"></a>

### First-time run
<a name="first-time-run"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Convert the PDF file. | Prepare the PDF file for your first-time run by splitting it into a single page and converting it into JPEG format for the Amazon Textract [synchronous operation](https://docs.aws.amazon.com/textract/latest/dg/sync.html) (`Syn API`).You can also use the Amazon Textract [asynchronous operation](https://docs.aws.amazon.com/textract/latest/dg/async.html) (`Asyn API`) for multipage PDF files. | Data scientist, Developer |
| Parse the Amazon Textract response JSON. | Open the `Textract_PostProcessing.ipynb` Jupyter notebook (attached) and call the Amazon Textract API by using the following code:<pre>response = textract.analyze_document(<br />Document={<br />        'S3Object': {<br />            'Bucket': BUCKET,<br />            'Name': '{}'.format(filename)<br />                    }<br />                },<br />        FeatureTypes=["TABLES", "FORMS"])</pre><br />Parse the response JSON into a form and table by using the following code:<pre>parseformKV=form_kv_from_JSON(response)<br />parseformTables=get_tables_fromJSON(response)</pre> | Data scientist, Developer |
| Edit the TemplateJSON file. | Edit the parsed JSON for each `KeyName` and corresponding `DataType` (for example, string, float, integer, or date), and table headers (for example, `ColumnNames` and `RowNames`).<br />This template is used for each individual PDF file type, which means that the template can be reused for PDF files that have an identical format. | Data scientist, Developer |
| Define the post-processing correction functions. | The values in Amazon Textract's response for the `TemplateJSON` file are strings. There is no differentiation for date, float, integer, or currency. These values must be converted to the correct data type for your downstream use case. <br />Correct each data type according to the `TemplateJSON` file by using the following code:<pre>finalJSON=postprocessingCorrection(parsedJSON,templateJSON)</pre> | Data scientist, Developer |

### Repeat run
<a name="repeat-run"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the PDF files. | Prepare the PDF files by splitting them into a single page and converting them into JPEG format for the Amazon Textract [synchronous operation](https://docs.aws.amazon.com/textract/latest/dg/sync.html) (`Syn API`).You can also use the Amazon Textract [asynchronous operation](https://docs.aws.amazon.com/textract/latest/dg/async.html) (`Asyn API`) for multipage PDF files. | Data scientist, Developer |
| Call the Amazon Textract API. | Call the Amazon Textract API by using the following code:<pre>response = textract.analyze_document(<br />        Document={<br />        'S3Object': {<br />            'Bucket': BUCKET,<br />            'Name': '{}'.format(filename)<br />                    }<br />                },<br />        FeatureTypes=["TABLES", "FORMS"])</pre> | Data scientist, Developer |
| Parse the Amazon Textract response JSON. | Parse the response JSON into a form and table by using the following code:<pre>parseformKV=form_kv_from_JSON(response)<br />parseformTables=get_tables_fromJSON(response)</pre> | Data scientist, Developer |
| Load the TemplateJSON file and match it with the parsed JSON. | Use the `TemplateJSON` file to extract the correct key-value pairs and table by using the following commands:<pre>form_kv_corrected=form_kv_correction(parseformKV,templateJSON)<br />form_table_corrected=form_Table_correction(parseformTables, templateJSON)<br />form_kv_table_corrected_final={**form_kv_corrected , **form_table_corrected}</pre> | Data scientist, Developer |
| Post-processing corrections. | Use `DataType` in the `TemplateJSON` file and post-processing functions to correct data by using the following code: <pre>finalJSON=postprocessingCorrection(form_kv_table_corrected_final,templateJSON)</pre> | Data scientist, Developer |

## Related resources
<a name="automatically-extract-content-from-pdf-files-using-amazon-textract-resources"></a>
+ [Automatically extract text and structured data from documents with Amazon Textract](https://aws.amazon.com/blogs/machine-learning/automatically-extract-text-and-structured-data-from-documents-with-amazon-textract/)
+ [Extract text and structured data with Amazon Textract ](https://aws.amazon.com/getting-started/hands-on/extract-text-with-amazon-textract/)
+ [Amazon Textract resources](https://aws.amazon.com/textract/resources/?blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc)

## Attachments
<a name="attachments-2d724523-2cab-42c9-a773-65857014d9ec"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/2d724523-2cab-42c9-a773-65857014d9ec/attachments/attachment.zip)
