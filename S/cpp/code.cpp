#include <iostream>
#include <string>
#include <vector>

using namespace std;

const string IPV4 = "IPv4";
const string IPV6 = "IPv6";
const string ERROR = "Error";


std::vector<std::string> split(const string& s, const string& delim) {
    std::vector<std::string> v;
    size_t pos = 0, pos2 = 0;
        while ((pos = s.find(delim, pos2)) != std::string::npos) {
            // std::cout << ", ";
            v.push_back(s.substr(pos2, pos - pos2));
            pos2 = pos + delim.length();
        }
        v.push_back(s.substr(pos2));
    return v;
}
/**
 * return IPV4,IPV6, or ERROR
 */
string checkIpAddress(const string& ip) {
    // auto it = ip.find(ip.begin(), ip.end(), '.');
    size_t pos = 0;
    if ((pos = ip.find(".")) != std::string::npos) {
        auto v = split(ip, ".");
        if (v.size() != 4)
            return ERROR;
        for (auto s : v) {
            // std::cout << s << ", ";
            if (s.length() > 1 && s[0] == '0')
                return ERROR;
            try {
                int i = stoi(s);
                if (i > 255 || i < 0)
                    return ERROR;
                for (const char c : s)
                    if (!(c >= '0' && c <= '9')) {
                        // std::cout << "Wrong char: " << c << '\n';
                        return ERROR;
                    }
            } catch (...) {
                return ERROR;
            }
            // 
        }
        // std::cout << '\n';
        return IPV4;
    } else if ((pos = ip.find(':')) != std::string::npos) {
        auto v = split(ip, ":");
        if (v.size() != 8)
            return ERROR;
        for (auto s : v) {
            if (s.length() > 4 || s.length() < 1)
                return ERROR;
            bool upperCase = false;
            bool lowerCase = false;
            for (const char c : s) {
                if (!((c >= '0' && c <= '9') || (c >= 'a' && c <= 'f') || (c >= 'A' && c <= 'F'))) {
                    // std::cout << "Wrong char: " << c << '\n';
                    return ERROR;                    
                }
                if (c >= 'a' && c <= 'f') {
                    if (upperCase)
                        return ERROR;
                    lowerCase = true;
                }
                if (c >= 'A' && c <= 'F') {
                    if (lowerCase)
                        return ERROR;
                    upperCase = true;
                }
            }
            
        }
        return IPV6;
    }

    return ERROR;
}

int main() {
    string ipAddress;
    cin >> ipAddress;
    cout << checkIpAddress(ipAddress);   
}