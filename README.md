# Snowflake to BigQuery ETL Pipeline with Apache Airflow

A complete ETL pipeline that extracts data from Snowflake, transforms it, and loads it into Google BigQuery using Apache Airflow and Astronomer.

## 🚀 Features

- **Snowflake Integration**: Extract data from Snowflake using Airflow hooks
- **Google Cloud Storage**: Upload transformed data to GCS
- **BigQuery Integration**: Load data into BigQuery with automatic table creation
- **Data Transformation**: Clean and transform data using Pandas
- **Connection Testing**: Comprehensive connection testing for all services
- **Astronomer Runtime**: Optimized for Astronomer Runtime 2.8-12

## 📋 Prerequisites

- Python 3.8+
- Apache Airflow 2.8+ (or Astronomer Runtime)
- Google Cloud Platform account with BigQuery and Cloud Storage enabled
- Snowflake account with sample data
- Docker (for local development with Astronomer)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd snowflake-airflow-bigquery
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
.\venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Connections

Update `airflow_settings.yaml` with your credentials:

```yaml
airflow:
  connections:
    - conn_id: snowflake_default
      conn_type: Snowflake
      conn_host: your-snowflake-host.snowflakecomputing.com
      conn_schema: your_schema
      conn_login: your_username
      conn_password: your_password
      conn_port: 443
      conn_extra:
        account: your-account
        database: your_database
    - conn_id: google_cloud_default
      conn_type: google_cloud_platform
      conn_extra:
        key_path: /usr/local/airflow/include/gcp/service_account.json
        project_id: your-gcp-project-id
        scope: https://www.googleapis.com/auth/cloud-platform
```

### 4. Set Up Google Cloud Service Account

1. Create a service account in Google Cloud Console
2. Download the JSON key file
3. Place it in `include/gcp/service_account.json`
4. Grant the following roles:
   - BigQuery Data Editor
   - Storage Object Admin
   - BigQuery Job User

### 5. Configure BigQuery

Create your dataset and update the configuration:

```bash
# Create BigQuery dataset
bq --location=US mk -d your_dataset_name
```

Update the configuration in your DAG files:
- `BQ_PROJECT`: Your GCP project ID
- `BQ_DATASET`: Your dataset name
- `GCS_BUCKET`: Your Cloud Storage bucket name

## 🏃‍♂️ Running the Pipeline

### Local Development with Astronomer

```bash
# Start Astronomer development environment
astro dev start

# Access Airflow UI
# http://localhost:8080
# Username: admin
# Password: admin
```

### Manual DAG Execution

1. Open Airflow UI
2. Navigate to your DAG
3. Click "Trigger DAG" to run manually

## 📁 Project Structure

```
snowflake-airflow-bigquery/
├── dags/
│   └── test_connections.py          # Connection testing DAG
├── include/
│   └── gcp/
│       └── service_account.json     # GCP service account key
├── airflow_settings.yaml            # Airflow connections configuration
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Docker configuration
├── .astro/
│   └── config.yaml                  # Astronomer configuration
└── README.md                        # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `BQ_PROJECT` | Google Cloud Project ID | `my-gcp-project` |
| `BQ_DATASET` | BigQuery Dataset Name | `analytics_data` |
| `GCS_BUCKET` | Cloud Storage Bucket | `my-data-bucket` |
| `SNOWFLAKE_CONN_ID` | Snowflake Connection ID | `snowflake_default` |
| `GCP_CONN_ID` | Google Cloud Connection ID | `google_cloud_default` |

### DAG Configuration

The main DAG (`test_connections.py`) includes:

- **Snowflake Connection Test**: Verifies Snowflake connectivity
- **GCS Upload Test**: Tests Cloud Storage upload functionality
- **BigQuery Query Test**: Executes a simple BigQuery query
- **Table Creation**: Creates BigQuery tables if they don't exist
- **Data Insertion**: Inserts test data into BigQuery

## 🔍 Testing Connections

The pipeline includes comprehensive connection testing:

1. **Snowflake Test**: Executes `SELECT 1` to verify connectivity
2. **GCS Test**: Uploads a test file to Cloud Storage
3. **BigQuery Test**: Runs a simple query and creates tables
4. **Data Insertion Test**: Inserts sample data into BigQuery

## 📊 Data Flow

```
Snowflake → Airflow Extract → Data Transformation → GCS Upload → BigQuery Load → Data Validation
```

## 🛡️ Security

- Service account keys are stored securely in `include/gcp/`
- Connections are configured in `airflow_settings.yaml`
- All sensitive data is externalized from code
- Follow principle of least privilege for service accounts

## 🐛 Troubleshooting

### Common Issues

1. **Connection Errors**
   - Verify credentials in `airflow_settings.yaml`
   - Check service account permissions
   - Ensure network connectivity

2. **BigQuery Table Not Found**
   - Run the table creation task first
   - Verify dataset exists in BigQuery
   - Check project ID configuration

3. **Authentication Errors**
   - Verify service account JSON file
   - Check GCP project permissions
   - Ensure service account has required roles

### Logs

Check Airflow logs for detailed error information:
- Airflow UI → DAGs → Your DAG → Task → Logs

## 📈 Monitoring

- Monitor DAG runs in Airflow UI
- Set up alerts for failed tasks
- Use Airflow's built-in metrics and logging
- Consider integrating with monitoring tools like Grafana

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:
- Check the troubleshooting section
- Review Airflow documentation
- Open an issue in this repository

## 🔄 Version History

- **v1.0.0**: Initial release with basic ETL pipeline
- **v1.1.0**: Added connection testing and error handling
- **v1.2.0**: Improved BigQuery integration and table management

---

**Note**: Remember to update the configuration variables with your actual project details before running the pipeline.