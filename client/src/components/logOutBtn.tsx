"use client"
import { Button } from "./ui/button";
import { signOut } from "next-auth/react";

export default function LogOutBtn() {
    return(
        <Button onClick={()=>{signOut()}}>Cerrar sesión</Button>
    )
}