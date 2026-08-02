---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-workload-assessment/storage.html
---

# Storage
<a name="storage"></a>

|
|
| Question | Example response |
| --- |--- |
| Where will the training data be stored? | In cloud storage (for example, Amazon S3, file storage, block storage, or object storage), in on-premises storage, and so on. |
| What are the storage requirements for the training data and model artifacts (for example, capacity, durability, availability)? | Petabyte-scale storage, high durability (99.999999999% durability), high availability, and so on. |
| What are the data retention and backup requirements for the training data and model artifacts? | Data retention for *x* years, daily backups, off-site backups, and so on. |
| Which file formats are primarily used for storing your AI training datasets (for example, CSV, JSON, Parquet, HDF5)? | Parquet files for structured data and HDF5 for large multidimensional arrays and unstructured data such as images and text. We use specialized formats such as TFRecord to optimize data loading during training. |
| How are your training datasets organized: as individual files, in databases, or using specialized AI data formats? | Small to medium datasets are stored as individual Parquet files in object storage for flexibility. Large datasets are stored in a distributed database (Cassandra) to handle scale. |
| Do you use any data compression or encoding techniques specifically for generative AI training data? | For tabular data, we use dictionary encoding and bit-packing techniques that are available in Parquet. For images, we use lossy JPEG compression with quality settings optimized for our models. |
| How do you handle versioning and storage of different iterations of training datasets? What impact does this have on your overall storage needs? | We use a data versioning system (DVC) that is integrated with our ML platform. |
