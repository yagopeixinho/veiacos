"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.userRoutes = void 0;
const express_1 = require("express");
const AuthUser_1 = require("../controllers/user/AuthUser");
const CreateUser_1 = require("../controllers/user/CreateUser");
const GetAllUsers_1 = require("../controllers/user/GetAllUsers");
const isAuthenticated_1 = require("../middlewares/isAuthenticated");
exports.userRoutes = (0, express_1.Router)();
exports.userRoutes.post("/", new CreateUser_1.CreateUserController().handle);
exports.userRoutes.post("/auth", new AuthUser_1.AuthUserController().handle);
exports.userRoutes.get("/", isAuthenticated_1.isAuthenticated, new GetAllUsers_1.GetAllUsersController().handle);
