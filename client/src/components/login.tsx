"use client"
import { useEffect } from "react";
import { signIn, useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { useForm } from "react-hook-form";
import { Input } from "./ui/input";
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormMessage,
} from "@/components/ui/form";

export default function Login() {
  const { data: session, status } = useSession()
  const form = useForm({
      defaultValues: {
        password: "",
        username: "",
      },
  });

  const router = useRouter();

  useEffect(() => {
      if (status === "authenticated") {
        router.push("/dashboard");
      }
  }, [status, router]);  

    
    const onSubmit = async (data) => {
      const result = await signIn("credentials", {
      username: data.username,
      password: data.password,
      redirect: false, 
    });

    if (result?.error) {
      console.error("Error al iniciar sesión:", result.error);
    } else {
      router.push("/dashboard");
    }
    };
    
    if (status === "loading") {
      return <p>Cargando...</p>;
    }
  
  
    return( 
      <>
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)} className=" w-full max-w-md space-y-4 p-6 bg-white rounded-md shadow-md flex flex-col justify-center">
          <FormField
          control={form.control} 
          name="username"
          rules = {{
            required: "The username is required"
          }} 
          render={({ field, fieldState: { error } }) => (
           <FormItem>
              <FormLabel>Username</FormLabel>
              <FormControl>
                <Input placeholder="Enter username" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>          
          )}
        />
          <FormField
          control={form.control}
          name="password"
          rules = {{
            required: "The password is required"
          }}          
          render={({ field, fieldState: { error } }) => (
           <FormItem>
              <FormLabel>Password</FormLabel>
              <FormControl>
                <Input type="password" placeholder="Enter password" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>          
          )}
        />
        <Button type="submit" className="mt-6">Iniciar sesión</Button>
      </form>
    </Form>  
      </>
    )
  }