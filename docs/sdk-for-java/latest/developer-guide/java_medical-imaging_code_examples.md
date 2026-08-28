---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/java_medical-imaging_code_examples.html
---

# HealthImaging examples using SDK for Java 2.x
<a name="java_medical-imaging_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Java 2.x with HealthImaging.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)
+ [Scenarios](#scenarios)

## Actions
<a name="actions"></a>

### `CopyImageSet`
<a name="medical-imaging_CopyImageSet_java_topic"></a>

The following code example shows how to use `CopyImageSet`.

**SDK for Java 2.x**

```
    /**
     * Copy an AWS HealthImaging image set.
     *
     * @param medicalImagingClient  - The AWS HealthImaging client object.
     * @param datastoreId           - The datastore ID.
     * @param imageSetId            - The image set ID.
     * @param latestVersionId       - The version ID.
     * @param destinationImageSetId - The optional destination image set ID, ignored if null.
     * @param destinationVersionId  - The optional destination version ID, ignored if null.
     * @param force                 - The force flag.
     * @param subsets               - The optional subsets to copy, ignored if null.
     * @return                      - The image set ID of the copy.
     * @throws MedicalImagingException - Base exception for all service exceptions thrown by AWS HealthImaging.
     */
    public static String copyMedicalImageSet(MedicalImagingClient medicalImagingClient,
                                             String datastoreId,
                                             String imageSetId,
                                             String latestVersionId,
                                             String destinationImageSetId,
                                             String destinationVersionId,
                                             boolean force,
                                             Vector<String> subsets) {

        try {
            CopySourceImageSetInformation.Builder copySourceImageSetInformation = CopySourceImageSetInformation.builder()
                    .latestVersionId(latestVersionId);

            // Optionally copy a subset of image instances.
            if (subsets != null) {
                String subsetInstanceToCopy = getCopiableAttributesJSON(imageSetId, subsets);
                copySourceImageSetInformation.dicomCopies(MetadataCopies.builder()
                        .copiableAttributes(subsetInstanceToCopy)
                        .build());
            }

            CopyImageSetInformation.Builder copyImageSetBuilder = CopyImageSetInformation.builder()
                    .sourceImageSet(copySourceImageSetInformation.build());

            // Optionally designate a destination image set.
            if (destinationImageSetId != null) {
                copyImageSetBuilder = copyImageSetBuilder.destinationImageSet(CopyDestinationImageSet.builder()
                        .imageSetId(destinationImageSetId)
                        .latestVersionId(destinationVersionId)
                        .build());
            }

            CopyImageSetRequest copyImageSetRequest = CopyImageSetRequest.builder()
                    .datastoreId(datastoreId)
                    .sourceImageSetId(imageSetId)
                    .copyImageSetInformation(copyImageSetBuilder.build())
                    .force(force)
                    .build();

            CopyImageSetResponse response = medicalImagingClient.copyImageSet(copyImageSetRequest);

            return response.destinationImageSetProperties().imageSetId();
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            throw e;
        }
    }
```
Utility function to create copiable attributes.

```
    /**
     * Create a JSON string of copiable image instances.
     *
     * @param imageSetId - The image set ID.
     * @param subsets    - The subsets to copy.
     * @return A JSON string of copiable image instances.
     */
    private static String getCopiableAttributesJSON(String imageSetId, Vector<String> subsets) {
        StringBuilder subsetInstanceToCopy = new StringBuilder(
                """
                        {
                          "SchemaVersion": 1.1,
                          "Study": {
                            "Series": {
                                "
                                 """
        );

        subsetInstanceToCopy.append(imageSetId);

        subsetInstanceToCopy.append(
                """
                                ": {
                                "Instances": {
                        """
        );

        for (String subset : subsets) {
            subsetInstanceToCopy.append('"' + subset + "\": {},");
        }
        subsetInstanceToCopy.deleteCharAt(subsetInstanceToCopy.length() - 1);
        subsetInstanceToCopy.append("""
                         }
                       }
                    }
                  }
                }
                """);
        return subsetInstanceToCopy.toString();
    }
```
+  For API details, see [CopyImageSet](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/CopyImageSet) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `CreateDatastore`
<a name="medical-imaging_CreateDatastore_java_topic"></a>

The following code example shows how to use `CreateDatastore`.

**SDK for Java 2.x**

```
    public static String createMedicalImageDatastore(MedicalImagingClient medicalImagingClient,
            String datastoreName) {
        try {
            CreateDatastoreRequest datastoreRequest = CreateDatastoreRequest.builder()
                    .datastoreName(datastoreName)
                    .build();
            CreateDatastoreResponse response = medicalImagingClient.createDatastore(datastoreRequest);
            return response.datastoreId();
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return "";
    }
```
+  For API details, see [CreateDatastore](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/CreateDatastore) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `DeleteDatastore`
<a name="medical-imaging_DeleteDatastore_java_topic"></a>

The following code example shows how to use `DeleteDatastore`.

**SDK for Java 2.x**

```
    public static void deleteMedicalImagingDatastore(MedicalImagingClient medicalImagingClient,
            String datastoreID) {
        try {
            DeleteDatastoreRequest datastoreRequest = DeleteDatastoreRequest.builder()
                    .datastoreId(datastoreID)
                    .build();
            medicalImagingClient.deleteDatastore(datastoreRequest);
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [DeleteDatastore](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/DeleteDatastore) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `DeleteImageSet`
<a name="medical-imaging_DeleteImageSet_java_topic"></a>

The following code example shows how to use `DeleteImageSet`.

**SDK for Java 2.x**

```
    public static void deleteMedicalImageSet(MedicalImagingClient medicalImagingClient,
            String datastoreId,
            String imagesetId) {
        try {
            DeleteImageSetRequest deleteImageSetRequest = DeleteImageSetRequest.builder()
                    .datastoreId(datastoreId)
                    .imageSetId(imagesetId)
                    .build();

            medicalImagingClient.deleteImageSet(deleteImageSetRequest);

            System.out.println("The image set was deleted.");
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [DeleteImageSet](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/DeleteImageSet) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `GetDICOMImportJob`
<a name="medical-imaging_GetDICOMImportJob_java_topic"></a>

The following code example shows how to use `GetDICOMImportJob`.

**SDK for Java 2.x**

```
    public static DICOMImportJobProperties getDicomImportJob(MedicalImagingClient medicalImagingClient,
            String datastoreId,
            String jobId) {

        try {
            GetDicomImportJobRequest getDicomImportJobRequest = GetDicomImportJobRequest.builder()
                    .datastoreId(datastoreId)
                    .jobId(jobId)
                    .build();
            GetDicomImportJobResponse response = medicalImagingClient.getDICOMImportJob(getDicomImportJobRequest);
            return response.jobProperties();
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return null;
    }
```
+  For API details, see [GetDICOMImportJob](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/GetDICOMImportJob) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `GetDatastore`
<a name="medical-imaging_GetDatastore_java_topic"></a>

The following code example shows how to use `GetDatastore`.

**SDK for Java 2.x**

```
    public static DatastoreProperties getMedicalImageDatastore(MedicalImagingClient medicalImagingClient,
            String datastoreID) {
        try {
            GetDatastoreRequest datastoreRequest = GetDatastoreRequest.builder()
                    .datastoreId(datastoreID)
                    .build();
            GetDatastoreResponse response = medicalImagingClient.getDatastore(datastoreRequest);
            return response.datastoreProperties();
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return null;
    }
```
+  For API details, see [GetDatastore](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/GetDatastore) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `GetImageFrame`
<a name="medical-imaging_GetImageFrame_java_topic"></a>

The following code example shows how to use `GetImageFrame`.

**SDK for Java 2.x**

```
        public static void getMedicalImageSetFrame(MedicalImagingClient medicalImagingClient,
                        String destinationPath,
                        String datastoreId,
                        String imagesetId,
                        String imageFrameId) {

                try {
                        GetImageFrameRequest getImageSetMetadataRequest = GetImageFrameRequest.builder()
                                        .datastoreId(datastoreId)
                                        .imageSetId(imagesetId)
                                        .imageFrameInformation(ImageFrameInformation.builder()
                                                        .imageFrameId(imageFrameId)
                                                        .build())
                                        .build();
                        medicalImagingClient.getImageFrame(getImageSetMetadataRequest,
                                        FileSystems.getDefault().getPath(destinationPath));

                        System.out.println("Image frame downloaded to " + destinationPath);
                } catch (MedicalImagingException e) {
                        System.err.println(e.awsErrorDetails().errorMessage());
                        System.exit(1);
                }
        }
```
+  For API details, see [GetImageFrame](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/GetImageFrame) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `GetImageSet`
<a name="medical-imaging_GetImageSet_java_topic"></a>

The following code example shows how to use `GetImageSet`.

**SDK for Java 2.x**

```
    public static GetImageSetResponse getMedicalImageSet(MedicalImagingClient medicalImagingClient,
            String datastoreId,
            String imagesetId,
            String versionId) {
        try {
            GetImageSetRequest.Builder getImageSetRequestBuilder = GetImageSetRequest.builder()
                    .datastoreId(datastoreId)
                    .imageSetId(imagesetId);

            if (versionId != null) {
                getImageSetRequestBuilder = getImageSetRequestBuilder.versionId(versionId);
            }

            return medicalImagingClient.getImageSet(getImageSetRequestBuilder.build());
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return null;
    }
```
+  For API details, see [GetImageSet](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/GetImageSet) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `GetImageSetMetadata`
<a name="medical-imaging_GetImageSetMetadata_java_topic"></a>

The following code example shows how to use `GetImageSetMetadata`.

**SDK for Java 2.x**

```
    public static void getMedicalImageSetMetadata(MedicalImagingClient medicalImagingClient,
            String destinationPath,
            String datastoreId,
            String imagesetId,
            String versionId) {

        try {
            GetImageSetMetadataRequest.Builder getImageSetMetadataRequestBuilder = GetImageSetMetadataRequest.builder()
                    .datastoreId(datastoreId)
                    .imageSetId(imagesetId);

            if (versionId != null) {
                getImageSetMetadataRequestBuilder = getImageSetMetadataRequestBuilder.versionId(versionId);
            }

            medicalImagingClient.getImageSetMetadata(getImageSetMetadataRequestBuilder.build(),
                    FileSystems.getDefault().getPath(destinationPath));

            System.out.println("Metadata downloaded to " + destinationPath);
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [GetImageSetMetadata](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/GetImageSetMetadata) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `ListDICOMImportJobs`
<a name="medical-imaging_ListDICOMImportJobs_java_topic"></a>

The following code example shows how to use `ListDICOMImportJobs`.

**SDK for Java 2.x**

```
    public static List<DICOMImportJobSummary> listDicomImportJobs(MedicalImagingClient medicalImagingClient,
            String datastoreId) {

        try {
            ListDicomImportJobsRequest listDicomImportJobsRequest = ListDicomImportJobsRequest.builder()
                    .datastoreId(datastoreId)
                    .build();
            ListDicomImportJobsResponse response = medicalImagingClient.listDICOMImportJobs(listDicomImportJobsRequest);
            return response.jobSummaries();
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return new ArrayList<>();
    }
```
+  For API details, see [ListDICOMImportJobs](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/ListDICOMImportJobs) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `ListDatastores`
<a name="medical-imaging_ListDatastores_java_topic"></a>

The following code example shows how to use `ListDatastores`.

**SDK for Java 2.x**

```
    public static List<DatastoreSummary> listMedicalImagingDatastores(MedicalImagingClient medicalImagingClient) {
        try {
            ListDatastoresRequest datastoreRequest = ListDatastoresRequest.builder()
                    .build();
            ListDatastoresIterable responses = medicalImagingClient.listDatastoresPaginator(datastoreRequest);
            List<DatastoreSummary> datastoreSummaries = new ArrayList<>();

            responses.stream().forEach(response -> datastoreSummaries.addAll(response.datastoreSummaries()));

            return datastoreSummaries;
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return null;
    }
```
+  For API details, see [ListDatastores](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/ListDatastores) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `ListImageSetVersions`
<a name="medical-imaging_ListImageSetVersions_java_topic"></a>

The following code example shows how to use `ListImageSetVersions`.

**SDK for Java 2.x**

```
    public static List<ImageSetProperties> listMedicalImageSetVersions(MedicalImagingClient medicalImagingClient,
            String datastoreId,
            String imagesetId) {
        try {
            ListImageSetVersionsRequest getImageSetRequest = ListImageSetVersionsRequest.builder()
                    .datastoreId(datastoreId)
                    .imageSetId(imagesetId)
                    .build();

            ListImageSetVersionsIterable responses = medicalImagingClient
                    .listImageSetVersionsPaginator(getImageSetRequest);
            List<ImageSetProperties> imageSetProperties = new ArrayList<>();
            responses.stream().forEach(response -> imageSetProperties.addAll(response.imageSetPropertiesList()));

            return imageSetProperties;
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return null;
    }
```
+  For API details, see [ListImageSetVersions](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/ListImageSetVersions) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `ListTagsForResource`
<a name="medical-imaging_ListTagsForResource_java_topic"></a>

The following code example shows how to use `ListTagsForResource`.

**SDK for Java 2.x**

```
    public static ListTagsForResourceResponse listMedicalImagingResourceTags(MedicalImagingClient medicalImagingClient,
            String resourceArn) {
        try {
            ListTagsForResourceRequest listTagsForResourceRequest = ListTagsForResourceRequest.builder()
                    .resourceArn(resourceArn)
                    .build();

            return medicalImagingClient.listTagsForResource(listTagsForResourceRequest);
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return null;
    }
```
+  For API details, see [ListTagsForResource](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/ListTagsForResource) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `SearchImageSets`
<a name="medical-imaging_SearchImageSets_java_topic"></a>

The following code example shows how to use `SearchImageSets`.

**SDK for Java 2.x**
The utility function for searching image sets.

```
    public static List<ImageSetsMetadataSummary> searchMedicalImagingImageSets(
            MedicalImagingClient medicalImagingClient,
            String datastoreId, SearchCriteria searchCriteria) {
        try {
            SearchImageSetsRequest datastoreRequest = SearchImageSetsRequest.builder()
                    .datastoreId(datastoreId)
                    .searchCriteria(searchCriteria)
                    .build();
            SearchImageSetsIterable responses = medicalImagingClient
                    .searchImageSetsPaginator(datastoreRequest);
            List<ImageSetsMetadataSummary> imageSetsMetadataSummaries = new ArrayList<>();

            responses.stream().forEach(response -> imageSetsMetadataSummaries
                    .addAll(response.imageSetsMetadataSummaries()));

            return imageSetsMetadataSummaries;
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return null;
    }
```
Use case \#1: EQUAL operator.

```
        List<SearchFilter> searchFilters = Collections.singletonList(SearchFilter.builder()
                .operator(Operator.EQUAL)
                .values(SearchByAttributeValue.builder()
                        .dicomPatientId(patientId)
                        .build())
                .build());

        SearchCriteria searchCriteria = SearchCriteria.builder()
                .filters(searchFilters)
                .build();

        List<ImageSetsMetadataSummary> imageSetsMetadataSummaries = searchMedicalImagingImageSets(
                medicalImagingClient,
                datastoreId, searchCriteria);
        if (imageSetsMetadataSummaries != null) {
            System.out.println("The image sets for patient " + patientId + " are:\n"
                    + imageSetsMetadataSummaries);
            System.out.println();
        }
```
Use case \#2: BETWEEN operator using DICOMStudyDate and DICOMStudyTime.

```
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyyMMdd");
        searchFilters = Collections.singletonList(SearchFilter.builder()
                .operator(Operator.BETWEEN)
                .values(SearchByAttributeValue.builder()
                                .dicomStudyDateAndTime(DICOMStudyDateAndTime.builder()
                                        .dicomStudyDate("19990101")
                                        .dicomStudyTime("000000.000")
                                        .build())
                                .build(),
                        SearchByAttributeValue.builder()
                                .dicomStudyDateAndTime(DICOMStudyDateAndTime.builder()
                                        .dicomStudyDate((LocalDate.now()
                                                .format(formatter)))
                                        .dicomStudyTime("000000.000")
                                        .build())
                                .build())
                .build());

        searchCriteria = SearchCriteria.builder()
                .filters(searchFilters)
                .build();

        imageSetsMetadataSummaries = searchMedicalImagingImageSets(medicalImagingClient,
                datastoreId, searchCriteria);
        if (imageSetsMetadataSummaries != null) {
            System.out.println(
                    "The image sets searched with BETWEEN operator using DICOMStudyDate and DICOMStudyTime are:\n"
                            +
                            imageSetsMetadataSummaries);
            System.out.println();
        }
```
Use case \#3: BETWEEN operator using createdAt. Time studies were previously persisted.

```
        searchFilters = Collections.singletonList(SearchFilter.builder()
                .operator(Operator.BETWEEN)
                .values(SearchByAttributeValue.builder()
                                .createdAt(Instant.parse("1985-04-12T23:20:50.52Z"))
                                .build(),
                        SearchByAttributeValue.builder()
                                .createdAt(Instant.now())
                                .build())
                .build());

        searchCriteria = SearchCriteria.builder()
                .filters(searchFilters)
                .build();
        imageSetsMetadataSummaries = searchMedicalImagingImageSets(medicalImagingClient,
                datastoreId, searchCriteria);
        if (imageSetsMetadataSummaries != null) {
            System.out.println("The image sets searched with BETWEEN operator using createdAt are:\n "
                    + imageSetsMetadataSummaries);
            System.out.println();
        }
```
Use case \#4: EQUAL operator on DICOMSeriesInstanceUID and BETWEEN on updatedAt and sort response in ASC order on updatedAt field.

```
        Instant startDate = Instant.parse("1985-04-12T23:20:50.52Z");
        Instant endDate = Instant.now();

        searchFilters = Arrays.asList(
                SearchFilter.builder()
                        .operator(Operator.EQUAL)
                        .values(SearchByAttributeValue.builder()
                                .dicomSeriesInstanceUID(seriesInstanceUID)
                                .build())
                        .build(),
                SearchFilter.builder()
                        .operator(Operator.BETWEEN)
                        .values(
                                SearchByAttributeValue.builder().updatedAt(startDate).build(),
                                SearchByAttributeValue.builder().updatedAt(endDate).build()
                        ).build());

        Sort sort = Sort.builder().sortOrder(SortOrder.ASC).sortField(SortField.UPDATED_AT).build();

        searchCriteria = SearchCriteria.builder()
                .filters(searchFilters)
                .sort(sort)
                .build();

        imageSetsMetadataSummaries = searchMedicalImagingImageSets(medicalImagingClient,
                datastoreId, searchCriteria);
        if (imageSetsMetadataSummaries != null) {
            System.out.println("The image sets searched with EQUAL operator on DICOMSeriesInstanceUID and BETWEEN on updatedAt and sort response\n" +
                    "in ASC order on updatedAt field are:\n "
                    + imageSetsMetadataSummaries);
            System.out.println();
        }
```
+  For API details, see [SearchImageSets](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/SearchImageSets) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `StartDICOMImportJob`
<a name="medical-imaging_StartDICOMImportJob_java_topic"></a>

The following code example shows how to use `StartDICOMImportJob`.

**SDK for Java 2.x**

```
    public static String startDicomImportJob(MedicalImagingClient medicalImagingClient,
            String jobName,
            String datastoreId,
            String dataAccessRoleArn,
            String inputS3Uri,
            String outputS3Uri) {

        try {
            StartDicomImportJobRequest startDicomImportJobRequest = StartDicomImportJobRequest.builder()
                    .jobName(jobName)
                    .datastoreId(datastoreId)
                    .dataAccessRoleArn(dataAccessRoleArn)
                    .inputS3Uri(inputS3Uri)
                    .outputS3Uri(outputS3Uri)
                    .build();
            StartDicomImportJobResponse response = medicalImagingClient.startDICOMImportJob(startDicomImportJobRequest);
            return response.jobId();
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return "";
    }
```
+  For API details, see [StartDICOMImportJob](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/StartDICOMImportJob) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `TagResource`
<a name="medical-imaging_TagResource_java_topic"></a>

The following code example shows how to use `TagResource`.

**SDK for Java 2.x**

```
    public static void tagMedicalImagingResource(MedicalImagingClient medicalImagingClient,
            String resourceArn,
            Map<String, String> tags) {
        try {
            TagResourceRequest tagResourceRequest = TagResourceRequest.builder()
                    .resourceArn(resourceArn)
                    .tags(tags)
                    .build();

            medicalImagingClient.tagResource(tagResourceRequest);

            System.out.println("Tags have been added to the resource.");
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/TagResource) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `UntagResource`
<a name="medical-imaging_UntagResource_java_topic"></a>

The following code example shows how to use `UntagResource`.

**SDK for Java 2.x**

```
    public static void untagMedicalImagingResource(MedicalImagingClient medicalImagingClient,
            String resourceArn,
            Collection<String> tagKeys) {
        try {
            UntagResourceRequest untagResourceRequest = UntagResourceRequest.builder()
                    .resourceArn(resourceArn)
                    .tagKeys(tagKeys)
                    .build();

            medicalImagingClient.untagResource(untagResourceRequest);

            System.out.println("Tags have been removed from the resource.");
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [UntagResource](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/UntagResource) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### `UpdateImageSetMetadata`
<a name="medical-imaging_UpdateImageSetMetadata_java_topic"></a>

The following code example shows how to use `UpdateImageSetMetadata`.

**SDK for Java 2.x**

```
    /**
     * Update the metadata of an AWS HealthImaging image set.
     *
     * @param medicalImagingClient - The AWS HealthImaging client object.
     * @param datastoreId          - The datastore ID.
     * @param imageSetId           - The image set ID.
     * @param versionId            - The version ID.
     * @param metadataUpdates      - A MetadataUpdates object containing the updates.
     * @param force                - The force flag.
     * @throws MedicalImagingException - Base exception for all service exceptions thrown by AWS HealthImaging.
     */
    public static void updateMedicalImageSetMetadata(MedicalImagingClient medicalImagingClient,
                                                     String datastoreId,
                                                     String imageSetId,
                                                     String versionId,
                                                     MetadataUpdates metadataUpdates,
                                                     boolean force) {
        try {
            UpdateImageSetMetadataRequest updateImageSetMetadataRequest = UpdateImageSetMetadataRequest
                    .builder()
                    .datastoreId(datastoreId)
                    .imageSetId(imageSetId)
                    .latestVersionId(versionId)
                    .updateImageSetMetadataUpdates(metadataUpdates)
                    .force(force)
                    .build();

            UpdateImageSetMetadataResponse response = medicalImagingClient.updateImageSetMetadata(updateImageSetMetadataRequest);

            System.out.println("The image set metadata was updated" + response);
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            throw e;
        }
    }
```
Use case \#1: Insert or update an attribute.

```
                final String insertAttributes = """
                        {
                          "SchemaVersion": 1.1,
                          "Study": {
                            "DICOM": {
                              "StudyDescription": "CT CHEST"
                            }
                          }
                        }
                        """;
                MetadataUpdates metadataInsertUpdates = MetadataUpdates.builder()
                        .dicomUpdates(DICOMUpdates.builder()
                                .updatableAttributes(SdkBytes.fromByteBuffer(
                                        ByteBuffer.wrap(insertAttributes
                                                .getBytes(StandardCharsets.UTF_8))))
                                .build())
                        .build();

                updateMedicalImageSetMetadata(medicalImagingClient, datastoreId, imagesetId,
                        versionid, metadataInsertUpdates, force);
```
Use case \#2: Remove an attribute.

```
                final String removeAttributes = """
                        {
                          "SchemaVersion": 1.1,
                          "Study": {
                            "DICOM": {
                              "StudyDescription": "CT CHEST"
                            }
                          }
                        }
                        """;
                MetadataUpdates metadataRemoveUpdates = MetadataUpdates.builder()
                        .dicomUpdates(DICOMUpdates.builder()
                                .removableAttributes(SdkBytes.fromByteBuffer(
                                        ByteBuffer.wrap(removeAttributes
                                                .getBytes(StandardCharsets.UTF_8))))
                                .build())
                        .build();

                updateMedicalImageSetMetadata(medicalImagingClient, datastoreId, imagesetId,
                        versionid, metadataRemoveUpdates, force);
```
Use case \#3: Remove an instance.

```
                final String removeInstance = """
                        {
                          "SchemaVersion": 1.1,
                          "Study": {
                            "Series": {
                              "1.1.1.1.1.1.12345.123456789012.123.12345678901234.1": {
                                "Instances": {
                                  "1.1.1.1.1.1.12345.123456789012.123.12345678901234.1": {}
                                }
                              }
                            }
                          }
                        }
                        """;
                MetadataUpdates metadataRemoveUpdates = MetadataUpdates.builder()
                        .dicomUpdates(DICOMUpdates.builder()
                                .removableAttributes(SdkBytes.fromByteBuffer(
                                        ByteBuffer.wrap(removeInstance
                                                .getBytes(StandardCharsets.UTF_8))))
                                .build())
                        .build();

                updateMedicalImageSetMetadata(medicalImagingClient, datastoreId, imagesetId,
                        versionid, metadataRemoveUpdates, force);
```
Use case \#4: Revert to a previous version.

```
                // In this case, revert to previous version.
                String revertVersionId = Integer.toString(Integer.parseInt(versionid) - 1);
                MetadataUpdates metadataRemoveUpdates = MetadataUpdates.builder()
                        .revertToVersionId(revertVersionId)
                        .build();
                updateMedicalImageSetMetadata(medicalImagingClient, datastoreId, imagesetId,
                        versionid, metadataRemoveUpdates, force);
```
+  For API details, see [UpdateImageSetMetadata](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/UpdateImageSetMetadata) in *AWS SDK for Java 2.x API Reference*.
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

## Scenarios
<a name="scenarios"></a>

### Tagging a data store
<a name="medical-imaging_Scenario_TaggingDataStores_java_topic"></a>

The following code example shows how to tag a HealthImaging data store.

**SDK for Java 2.x**
To tag a data store.

```
                final String datastoreArn = "arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012";

                TagResource.tagMedicalImagingResource(medicalImagingClient, datastoreArn,
                                ImmutableMap.of("Deployment", "Development"));
```
The utility function for tagging a resource.

```
    public static void tagMedicalImagingResource(MedicalImagingClient medicalImagingClient,
            String resourceArn,
            Map<String, String> tags) {
        try {
            TagResourceRequest tagResourceRequest = TagResourceRequest.builder()
                    .resourceArn(resourceArn)
                    .tags(tags)
                    .build();

            medicalImagingClient.tagResource(tagResourceRequest);

            System.out.println("Tags have been added to the resource.");
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
To list tags for a data store.

```
                final String datastoreArn = "arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012";

                ListTagsForResourceResponse result = ListTagsForResource.listMedicalImagingResourceTags(
                                medicalImagingClient,
                                datastoreArn);
                if (result != null) {
                        System.out.println("Tags for resource: " + result.tags());
                }
```
The utility function for listing a resource's tags.

```
    public static ListTagsForResourceResponse listMedicalImagingResourceTags(MedicalImagingClient medicalImagingClient,
            String resourceArn) {
        try {
            ListTagsForResourceRequest listTagsForResourceRequest = ListTagsForResourceRequest.builder()
                    .resourceArn(resourceArn)
                    .build();

            return medicalImagingClient.listTagsForResource(listTagsForResourceRequest);
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return null;
    }
```
To untag a data store.

```
                final String datastoreArn = "arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012";

                UntagResource.untagMedicalImagingResource(medicalImagingClient, datastoreArn,
                                Collections.singletonList("Deployment"));
```
The utility function for untagging a resource.

```
    public static void untagMedicalImagingResource(MedicalImagingClient medicalImagingClient,
            String resourceArn,
            Collection<String> tagKeys) {
        try {
            UntagResourceRequest untagResourceRequest = UntagResourceRequest.builder()
                    .resourceArn(resourceArn)
                    .tagKeys(tagKeys)
                    .build();

            medicalImagingClient.untagResource(untagResourceRequest);

            System.out.println("Tags have been removed from the resource.");
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [ListTagsForResource](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/ListTagsForResource)
  + [TagResource](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/TagResource)
  + [UntagResource](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/UntagResource)
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

### Tagging an image set
<a name="medical-imaging_Scenario_TaggingImageSets_java_topic"></a>

The following code example shows how to tag a HealthImaging image set.

**SDK for Java 2.x**
To tag an image set.

```
                final String imageSetArn = "arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012/imageset/12345678901234567890123456789012";

                TagResource.tagMedicalImagingResource(medicalImagingClient, imageSetArn,
                                ImmutableMap.of("Deployment", "Development"));
```
The utility function for tagging a resource.

```
    public static void tagMedicalImagingResource(MedicalImagingClient medicalImagingClient,
            String resourceArn,
            Map<String, String> tags) {
        try {
            TagResourceRequest tagResourceRequest = TagResourceRequest.builder()
                    .resourceArn(resourceArn)
                    .tags(tags)
                    .build();

            medicalImagingClient.tagResource(tagResourceRequest);

            System.out.println("Tags have been added to the resource.");
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
To list tags for an image set.

```
                final String imageSetArn = "arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012/imageset/12345678901234567890123456789012";

                ListTagsForResourceResponse result = ListTagsForResource.listMedicalImagingResourceTags(
                                medicalImagingClient,
                                imageSetArn);
                if (result != null) {
                        System.out.println("Tags for resource: " + result.tags());
                }
```
The utility function for listing a resource's tags.

```
    public static ListTagsForResourceResponse listMedicalImagingResourceTags(MedicalImagingClient medicalImagingClient,
            String resourceArn) {
        try {
            ListTagsForResourceRequest listTagsForResourceRequest = ListTagsForResourceRequest.builder()
                    .resourceArn(resourceArn)
                    .build();

            return medicalImagingClient.listTagsForResource(listTagsForResourceRequest);
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return null;
    }
```
To untag an image set.

```
                final String imageSetArn = "arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012/imageset/12345678901234567890123456789012";

                UntagResource.untagMedicalImagingResource(medicalImagingClient, imageSetArn,
                                Collections.singletonList("Deployment"));
```
The utility function for untagging a resource.

```
    public static void untagMedicalImagingResource(MedicalImagingClient medicalImagingClient,
            String resourceArn,
            Collection<String> tagKeys) {
        try {
            UntagResourceRequest untagResourceRequest = UntagResourceRequest.builder()
                    .resourceArn(resourceArn)
                    .tagKeys(tagKeys)
                    .build();

            medicalImagingClient.untagResource(untagResourceRequest);

            System.out.println("Tags have been removed from the resource.");
        } catch (MedicalImagingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+ For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.
  + [ListTagsForResource](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/ListTagsForResource)
  + [TagResource](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/TagResource)
  + [UntagResource](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/UntagResource)
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/medicalimaging#code-examples).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
