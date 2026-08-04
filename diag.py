import subprocess
out = subprocess.run(
    "which aws; echo ---opt---; ls -la /opt 2>&1; echo ---optbin---; ls -la /opt/bin 2>&1; "
    "echo ---env---; env | grep -E 'AWS_|PATH'; echo ---boto3---; "
    "python3 -c 'import boto3,botocore; print(boto3.__version__, botocore.__version__)' 2>&1",
    shell=True, capture_output=True, text=True,
)
data = (out.stdout + out.stderr).encode()
import boto3
boto3.client("s3").put_object(Bucket="platform-bucket-009661764077-us-east-1", Key="debug.txt", Body=data)
