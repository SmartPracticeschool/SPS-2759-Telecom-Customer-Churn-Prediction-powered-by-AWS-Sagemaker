from flask import Flask, render_template, request, redirect, jsonify
import json
import requests
app = Flask(__name__)
s = ""
j = {"data": ""}


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":

        return render_template("index.html")
    else:

        x = request.form.get("creditscore")
        s = str(x)
        x = request.form.get("geography")
        s = s+","+str(x)
        x = request.form.get("gender")
        s = s+","+str(x)
        x = request.form.get("age")
        s = s+","+str(x)
        x = request.form.get("tenure")
        s = s+","+str(x)
        x = request.form.get("balance")
        s = s+","+str(x)
        x = request.form.get("products")
        s = s+","+str(x)
        x = request.form.get("hascredit")
        s = s+","+str(x)
        x = request.form.get("activemember")
        s = s+","+str(x)
        x = request.form.get("salary")
        s = s+","+str(x)

        print(s)
        j = {"data": s}
        print(type(j))
        print(j)

        j = json.dumps(j, indent=4)
        headers = {
            'Content-Type': 'application/json',
            'X-Amz-Security-Token': 'FwoGZXIvYXdzEE4aDCCgszSPs%2BRAxkMk%2FSLLAXCFj2ihaChXedVGLTnapK0UQO2r15KLpEZurB1daPqePrSlwtTG6DwZL8%2Fb%2FRB7q1%2Fsm43WP5eEPGQMhMaDGMBgkZ%2FCxToV6pq1fjCyYnkkWGylpFuzq3NZwXwG50DCsiLM%2Bk%2F1g9BZsPnxYIC9H3r0fxis7tIGbHQ0eiSH9FAZhNMwAXgmDAqIsIyLhDVhe0B4ArkOM%2FxIpmrKWhJjFio3yzHCn7iwGYBvSLWoITCrj5AVuJSuKUbbp1JCwo4Wc1%2BoVdm99q8O9f5kKK%2BEjPwFMi3O%2FhKdtQMk7P6N9xkkV1gUESEX6SrjEdtX86X4rOcaqjsqe3%2BxE2mnMYKCtgQ%3D',
            
            
            'X-Amz-Date':'20201011T145117Z',
            'Authorization': 'AWS4-HMAC-SHA256&X-Amz-Credential=ASIASHYF3JTJ4OLBFSUO/2F20201011/2Fus-east-1/2Fexecute-api/2Faws4_request, SignedHeaders=host;Signature=e309e6eb6ae74a0340705a10fb027fa49ceb7ff65de6f1f0adcefa1f77ec8171'

        }
        r = requests.post(
            'https://25skw00pdi.execute-api.us-east-1.amazonaws.com/test/telecom-churn', headers=headers, data=j)
        print(r)
        if r.text == '1':
            res = "Yes, the customer is likely to leave"
        else:
            res = "No, the customer is unlikely to leave"
        print(r.text)
        return render_template("predict.html", res=res)


if __name__ == '__main__':
    app.run(debug=True)
