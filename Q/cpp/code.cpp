#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

struct Point {
    long long x;
    long long y;

    Point(long long x, long long y): x(x), y(y) {
    }
};


bool isOnOneLine(const vector<Point>& points) {
    // your code goes here
    if (points.size() < 3)
        return true;

    if (points[1].x == points[0].x && points[1].y == points[0].y)
        return isOnOneLine({points.begin() + 1, points.end()});

    if (points[1].x != points[0].x) {
        double a  = static_cast<double>(points[1].y - points[0].y) / (points[1].x - points[0].x);
        double b = points[0].y - a * points[0].x;
        // cout << "a: " << a << ", b: " << b << '\n';
        double e = 1e-18;
        // std::cout << e << '\n';
        for (auto p : points) {
            // if (p.y + p.y*e < a * p.x + b || p.y - p.y*e > a * p.x + b) {
            //     std::cout << "py*e: " << p.y*e << ", ():" << a * p.x + b << '\n';

            if (p.y != round(a * p.x + b)) {
                // std::cout << "py: " << p.y << ", ():" << round(a * p.x + b) << '\n';
                return false;
            }
        }
        return true;
    } else {
        for (auto p : points) {
            if (p.x != points[0].x)
                return false;
        }
        return true;
    }


    return false;
}

int main() {
    int n;
    cin >> n;
    vector<Point> points;
    for (int i = 0; i < n; i++) {
        long long x, y;
        cin >> x >> y;
        points.push_back(Point(x, y));
    }
    if (isOnOneLine(points)) {
        cout << "YES";
    } else {
        cout << "NO";
    }
}