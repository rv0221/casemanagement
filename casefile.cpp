#include <iostream>
#include <fstream>
#include <cstring>
#include <conio.h>
#include <windows.h>
using namespace std;

class DATE {
    int dd, mm, yy;
public:
    DATE() { dd = mm = yy = 0; }
    void enterdate() { cin >> dd >> mm >> yy; }
    void showdate() { cout << dd << "/" << mm << "/" << yy; }
};

class CASE {
    int caseno;
    char courtname[50], title[50], add[200], clientname[20], stageofcase[100];
    char casetype[20], act[50];
    DATE doi, doj, nextdate;
    int choice;

public:
    CASE() {
        caseno = 0;
        strcpy(courtname, "NULL");
        strcpy(title, "NULL");
        strcpy(add, "NULL");
        strcpy(clientname, "NULL");
        strcpy(stageofcase, "NULL");
        strcpy(casetype, "NULL");
        strcpy(act, "NULL");
    }
    void enterdetails();
    void showdetails();
    int getcaseno() { return caseno; }
};

void CASE::enterdetails() {
    cout << "\n Enter Name of Client: ";
    cin.ignore();
    cin.getline(clientname, 20);
    cout << "\n Enter Address of Client: ";
    cin.getline(add, 200);
    cout << "\n Enter Case Number: ";
    cin >> caseno;
    cout << "\n Enter Date of Institution: ";
    doi.enterdate();
    cout << "\n Enter Case Type: ";
    cin.ignore();
    cin.getline(casetype, 20);
    cout << "\n Enter Court Name: ";
    cin.getline(courtname, 50);
    cout << "\n Enter Section(s)/Act(s): ";
    cin.getline(act, 50);
    cout << "\n Enter Title of the Case: ";
    cin.getline(title, 50);
    cout << "\n Enter Next Date of Hearing: ";
    nextdate.enterdate();
    cout << "\n Enter Stage of Case: ";
    cin.getline(stageofcase, 100);
    cout << "\n Enter Date of Judgement: ";
    doj.enterdate();
}

void CASE::showdetails() {
    cout << "\n Name of Client: " << clientname;
    cout << "\n Address of Client: " << add;
    cout << "\n Case Number: " << caseno;
    cout << "\n Date of Institution: ";
    doi.showdate();
    cout << "\n Case Type: " << casetype;
    cout << "\n Court Name: " << courtname;
    cout << "\n Section(s)/Act(s): " << act;
    cout << "\n Title of the Case: " << title;
    cout << "\n Next Date of Hearing: ";
    nextdate.showdate();
    cout << "\n Stage of Case: " << stageofcase;
    cout << "\n Date of Judgement: ";
    doj.showdate();
}

void add_case();
void display_cases();
void delete_case();
void modify_case();
void loading_screen();

int main() {
    int choice;
    loading_screen();
    while (true) {
        system("cls");
        cout << "\n Lawyer Case Management System";
        cout << "\n 1. Add Case";
        cout << "\n 2. Display Cases";
        cout << "\n 3. Delete Case";
        cout << "\n 4. Modify Case";
        cout << "\n 5. Exit";
        cout << "\n Enter choice: ";
        cin >> choice;
        switch (choice) {
        case 1: add_case(); break;
        case 2: display_cases(); break;
        case 3: delete_case(); break;
        case 4: modify_case(); break;
        case 5: exit(0);
        default: cout << "\n Invalid choice!";
        }
        getch();
    }
    return 0;
}

void add_case() {
    ofstream file("cases.dat", ios::binary | ios::app);
    CASE obj;
    obj.enterdetails();
    file.write((char*)&obj, sizeof(obj));
    file.close();
    cout << "\n Case added successfully!";
}

void display_cases() {
    ifstream file("cases.dat", ios::binary);
    CASE obj;
    while (file.read((char*)&obj, sizeof(obj))) {
        obj.showdetails();
        cout << "\n--------------------------------------";
    }
    file.close();
}

void delete_case() {
    int num;
    cout << "\n Enter Case Number to delete: ";
    cin >> num;
    ifstream file("cases.dat", ios::binary);
    ofstream temp("temp.dat", ios::binary);
    CASE obj;
    bool found = false;
    while (file.read((char*)&obj, sizeof(obj))) {
        if (obj.getcaseno() != num)
            temp.write((char*)&obj, sizeof(obj));
        else
            found = true;
    }
    file.close();
    temp.close();
    remove("cases.dat");
    rename("temp.dat", "cases.dat");
    if (found)
        cout << "\n Case deleted successfully!";
    else
        cout << "\n Case not found!";
}

void modify_case() {
    int num;
    cout << "\n Enter Case Number to modify: ";
    cin >> num;
    fstream file("cases.dat", ios::binary | ios::in | ios::out);
    CASE obj;
    bool found = false;
    while (file.read((char*)&obj, sizeof(obj)) && !found) {
        if (obj.getcaseno() == num) {
            cout << "\n Enter new details: ";
            obj.enterdetails();
            int pos = -1 * static_cast<int>(sizeof(obj));
            file.seekp(pos, ios::cur);
            file.write((char*)&obj, sizeof(obj));
            found = true;
        }
    }
    file.close();
    if (found)
        cout << "\n Case modified successfully!";
    else
        cout << "\n Case not found!";
}

void loading_screen() {
    cout << "\n Loading";
    for (int i = 0; i < 5; i++) {
        Sleep(500);
        cout << ".";
    }
    cout << "\n Ready!";
}
