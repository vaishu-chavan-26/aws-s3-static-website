import boto3

bucket_name = "vaishnavi-static-site-123"
file_name = "index.html"

s3 = boto3.client('s3')

try:
    s3.upload_file(
        file_name,
        bucket_name,
        file_name,
        ExtraArgs={'ContentType': 'text/html'}   # 🔥 THIS LINE FIXES IT
    )
    print("✅ File uploaded successfully!")
except Exception as e:
    print("❌ Error:", e)