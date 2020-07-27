from centos:latest
maintainer "Arix J"
run yum install -y python36 
run pip3 install -r requirements.txt
copy mnist.py /root/
copy input.txt /root/
copy accuracy_report.txt /root/
entrypoint ["python3"]
cmd ["/root/mnist.py"]