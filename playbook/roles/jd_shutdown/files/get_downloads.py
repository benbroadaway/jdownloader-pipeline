import myjdapi
import sys


def is_finished(link):
  if "finished" in link.keys():
    return link["finished"]
  else:
    return False



if len(sys.argv) < 4:
  print("Invalid arguments. Two parameters are required: my_jd_email my_jd_password device_name")
  exit(1)

email=str(sys.argv[1])
password=str(sys.argv[2])
device_name=str(sys.argv[3])

jd=myjdapi.Myjdapi()
jd.set_app_key("jd.ansible.pipeline")

# connect to api
jd.connect(email, password)
jd.update_devices()

dev = jd.get_device(device_name)

# get current state of downloads
downloadState = dev.downloadcontroller.get_current_state()
# print("Current state: " + downloadState)

# current links
links = dev.downloads.query_links()

# if running... let it be

# if downloadState == "RUNNING":
  # print("Downloads are running.")
  # exit(0)

# if stopped, and more downloads left...do something
unfinishedItems = list(filter(lambda link: is_finished(link) == False, links))

if (len(unfinishedItems) > 0):
  # print("There are " + str(len(unfinishedItems)) + " unfinished downloads")
  print(str(len(unfinishedItems)))
  exit(0)
else:
  print(0)
  exit(0)


# we shouldn't get this far
print("Finished with unexpected error.")
exit(1)



# print( urllib.parse.quote(email))

# def get_secret(email, password, domain):
#   print("email: " + email)
#   print("password: " + password)
#   print("domain: " + domain)
#   encodedEmail = urllib.parse.quote(email)
#   return encode_string_to_sha256(encodedEmail + password + domain)

# def encode_string_to_sha256(text):
#   print( "encoding: " + text)
#   hash_object = hashlib.sha256(text.encode())
#   hex_dig = hash_object.hexdigest()
#   return hex_dig

# def get_signature(data, key):
#   dataBytes = data.encode()
#   return base64.b64encode(hmac.new(secret, dataBytes, digestmod=hashlib.sha256).digest())


# message = bytes('Message', 'utf-8')
# secret = bytes('secret', 'utf-8')



# loginSecret = get_secret(email, password, "server")
# print("loginSecret: " + loginSecret)

# # build the full queryString (incl. RequestID)
# queryString = "/my/connect?email=" + urllib.parse.quote(email) + "&rid=" + str(rid)

# # hmac the queryString. The used Key depends. Some calls use serverEncryptionToken, others have to ask the user for email and password, create the loginSecret and use the loginsecret as key. email needs to be lower case!

# loginSecret = get_secret(email, password, "server")
# queryString += "&signature=" + get_signature(queryString, loginSecret.encode())
# print(queryString)

# "/my/connect?email={HttpUtility.UrlEncode(email)}&appkey={HttpUtility.UrlEncode(Utils.AppKey)}"
# loginSecret = get_secret(email, password, "server")

# #3 hexformat the result
# #4 append the signature to the queryString &signature=.
