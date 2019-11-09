CREATE DATABASE `tester2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
CREATE TABLE `address` (
  `CID` int(11) NOT NULL,
  `Address` varchar(45) NOT NULL,
  PRIMARY KEY (`CID`,`Address`),
  CONSTRAINT `CID` FOREIGN KEY (`CID`) REFERENCES `contact detail` (`ContactID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `author` (
  `AuthorID` int(11) NOT NULL,
  `Fname` varchar(45) NOT NULL,
  `Lname` varchar(45) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `DOB` varchar(12) NOT NULL,
  `CID2` int(11) DEFAULT NULL,
  PRIMARY KEY (`AuthorID`),
  KEY `CID3_idx` (`CID2`),
  CONSTRAINT `CID2` FOREIGN KEY (`CID2`) REFERENCES `contact detail` (`ContactID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `book` (
  `ISBN` int(11) NOT NULL COMMENT 'ISBN to book',
  `Title` varchar(45) NOT NULL,
  `Publish Date` date NOT NULL,
  `Price` int(11) NOT NULL,
  PRIMARY KEY (`ISBN`),
  UNIQUE KEY `ISBN_UNIQUE` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='this is a book';
CREATE TABLE `categorized` (
  `ISBN` int(11) NOT NULL,
  `CategoryCode` int(11) NOT NULL,
  PRIMARY KEY (`ISBN`,`CategoryCode`),
  KEY `CategoryCode_idx` (`CategoryCode`),
  CONSTRAINT `CategoryCode` FOREIGN KEY (`CategoryCode`) REFERENCES `category` (`CategoryCode`),
  CONSTRAINT `ISBN` FOREIGN KEY (`ISBN`) REFERENCES `book` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `category` (
  `CategoryCode` int(11) NOT NULL,
  `CategoryDescription` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`CategoryCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `contact detail` (
  `ContactID` int(11) NOT NULL,
  PRIMARY KEY (`ContactID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `customers` (
  `CustomerID` int(11) NOT NULL,
  `First name` varchar(45) NOT NULL,
  `Last Name` varchar(45) NOT NULL,
  `CID3` int(11) NOT NULL,
  PRIMARY KEY (`CustomerID`),
  KEY `ContactID_idx` (`CID3`),
  CONSTRAINT `CID3` FOREIGN KEY (`CID3`) REFERENCES `contact detail` (`ContactID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `email` (
  `CID` int(11) NOT NULL,
  `Email` varchar(45) NOT NULL,
  PRIMARY KEY (`CID`,`Email`),
  CONSTRAINT `ContactD` FOREIGN KEY (`CID`) REFERENCES `contact detail` (`ContactID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `order` (
  `OrderId` int(11) NOT NULL,
  `Order_Date` date NOT NULL,
  `Order_Value` int(11) NOT NULL,
  `CuID` int(11) NOT NULL,
  PRIMARY KEY (`OrderId`),
  KEY `CID_idx` (`CuID`),
  CONSTRAINT `CuID` FOREIGN KEY (`CuID`) REFERENCES `customers` (`CustomerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `orderitems` (
  `Item_Number` int(11) NOT NULL,
  `Item_Price` int(11) NOT NULL,
  `OrderID2` int(11) NOT NULL,
  `ISBN2` int(11) NOT NULL,
  PRIMARY KEY (`Item_Number`),
  KEY `OrderID_idx` (`OrderID2`),
  KEY `ISBN_idx` (`ISBN2`),
  CONSTRAINT `ISBN2` FOREIGN KEY (`ISBN2`) REFERENCES `book` (`ISBN`),
  CONSTRAINT `OrderID2` FOREIGN KEY (`OrderID2`) REFERENCES `order` (`OrderId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `phone` (
  `CuID2` int(11) NOT NULL,
  `Number` int(11) NOT NULL,
  PRIMARY KEY (`Number`),
  KEY `CuID2_idx` (`CuID2`),
  CONSTRAINT `CuID2` FOREIGN KEY (`CuID2`) REFERENCES `customers` (`CustomerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `supplier` (
  `Name` varchar(45) NOT NULL,
  PRIMARY KEY (`Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `supplierrep` (
  `Id` int(11) NOT NULL,
  `First_Name` varchar(45) NOT NULL,
  `Last_Name` varchar(45) NOT NULL,
  `Cell_Num` int(11) NOT NULL,
  `Work_Num` int(11) NOT NULL,
  `Email` varchar(45) NOT NULL,
  PRIMARY KEY (`Id`,`First_Name`,`Last_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `user review` (
  `ISBN3` int(11) NOT NULL,
  `Review` varchar(45) NOT NULL,
  `User Reviewcol` varchar(45) NOT NULL,
  PRIMARY KEY (`ISBN3`,`Review`),
  CONSTRAINT `ISBN3` FOREIGN KEY (`ISBN3`) REFERENCES `book` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `writes` (
  `AuthorID2` int(11) NOT NULL,
  `ISBN4` int(11) NOT NULL,
  KEY `ISBN4_idx` (`ISBN4`),
  KEY `AuthorID2_idx` (`AuthorID2`),
  CONSTRAINT `AuthorID2` FOREIGN KEY (`AuthorID2`) REFERENCES `author` (`AuthorID`),
  CONSTRAINT `ISBN4` FOREIGN KEY (`ISBN4`) REFERENCES `book` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
