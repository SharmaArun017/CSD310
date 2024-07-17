CREATE DATABASE BacchusWinery;
USE BacchusWinery;

-- Create tables
CREATE TABLE Wine (
    WineID INT PRIMARY KEY AUTO_INCREMENT,
    WineName VARCHAR(50),
    Type VARCHAR(50),
    Price DECIMAL(10, 2)
);

CREATE TABLE Supplier (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,
    SupplierName VARCHAR(100),
    ContactInfo VARCHAR(100)
);

CREATE TABLE Supply (
    SupplyID INT PRIMARY KEY AUTO_INCREMENT,
    SupplyType VARCHAR(50),
    Quantity INT,
    SupplierID INT,
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
);

CREATE TABLE Distributor (
    DistributorID INT PRIMARY KEY AUTO_INCREMENT,
    DistributorName VARCHAR(100),
    ContactInfo VARCHAR(100)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    OrderDate DATE,
    DistributorID INT,
    FOREIGN KEY (DistributorID) REFERENCES Distributor(DistributorID)
);

CREATE TABLE OrderDetails (
    OrderDetailsID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    WineID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (WineID) REFERENCES Wine(WineID)
);

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    EmployeeName VARCHAR(100),
    Department VARCHAR(50),
    HoursWorked INT
);

-- Insert sample data
INSERT INTO Wine (WineName, Type, Price) VALUES 
('Merlot', 'Red', 15.50), 
('Cabernet', 'Red', 20.00), 
('Chablis', 'White', 12.75), 
('Chardonnay', 'White', 18.25);

INSERT INTO Supplier (SupplierName, ContactInfo) VALUES 
('Bottle Supplier', '123-456-7890'),
('Label Supplier', '234-567-8901'),
('Vats Supplier', '345-678-9012');

INSERT INTO Supply (SupplyType, Quantity, SupplierID) VALUES 
('Bottles', 1000, 1), 
('Corks', 2000, 1), 
('Labels', 1500, 2), 
('Boxes', 500, 2), 
('Vats', 10, 3), 
('Tubing', 100, 3);

INSERT INTO Distributor (DistributorName, ContactInfo) VALUES 
('Wine Distributors Inc.', '456-789-0123'),
('Global Wines', '567-890-1234'),
('Local Wine Shop', '678-901-2345');

INSERT INTO Orders (OrderDate, DistributorID) VALUES 
('2024-07-01', 1), 
('2024-07-02', 2), 
('2024-07-03', 3);

INSERT INTO OrderDetails (OrderID, WineID, Quantity) VALUES 
(1, 1, 50), 
(1, 2, 30), 
(2, 3, 20), 
(2, 4, 25), 
(3, 1, 15), 
(3, 3, 10);

INSERT INTO Employee (EmployeeName, Department, HoursWorked) VALUES 
('Janet Collins', 'Finance', 160), 
('Roz Murphy', 'Marketing', 150), 
('Bob Ulrich', 'Marketing', 140), 
('Henry Doyle', 'Production', 170), 
('Maria Costanza', 'Distribution', 155), 
('Stan Bacchus', 'Management', 180);
